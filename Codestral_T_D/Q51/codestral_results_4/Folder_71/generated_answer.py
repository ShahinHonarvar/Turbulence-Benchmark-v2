from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    anagram_count = 0
    for key in anagrams:
        anagram_count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return anagram_count <= 9