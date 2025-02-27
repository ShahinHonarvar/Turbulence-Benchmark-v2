from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                count += len(anagrams[sorted_word])
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    return count <= 93