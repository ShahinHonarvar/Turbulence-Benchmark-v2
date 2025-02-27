from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word] = anagrams.get(sorted_word, 0) + 1
    return sum((n * (n - 1) // 2 for n in anagrams.values())) <= 181