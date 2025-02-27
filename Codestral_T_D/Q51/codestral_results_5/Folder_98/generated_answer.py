from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    anagram_pairs = sum([len(anagrams[key]) * (len(anagrams[key]) - 1) // 2 for key in anagrams if len(anagrams[key]) > 1])
    return anagram_pairs <= 46