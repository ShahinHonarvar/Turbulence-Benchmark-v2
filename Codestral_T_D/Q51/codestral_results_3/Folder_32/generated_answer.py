from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_count += anagram_dict[sorted_word]
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    return anagram_count <= 89