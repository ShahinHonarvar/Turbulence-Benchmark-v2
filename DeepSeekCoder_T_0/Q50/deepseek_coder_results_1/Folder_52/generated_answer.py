from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(int)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return pairs >= 58