from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            d[sorted_word] += 1
    count = sum((v * (v - 1) // 2 for v in d.values()))
    return count <= 86