from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            d[sorted_word] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in d.values()))
    return anagram_pairs <= 445