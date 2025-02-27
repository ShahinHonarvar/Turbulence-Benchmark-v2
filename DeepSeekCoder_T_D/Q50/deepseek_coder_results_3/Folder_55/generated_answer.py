from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagrams.values()))
    return pairs >= 15