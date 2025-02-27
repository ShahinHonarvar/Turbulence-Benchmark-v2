from collections import defaultdict

def if_contains_anagrams(lst):
    counter = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            counter[sorted_word] += 1
    pairs = sum((v * (v - 1) // 2 for v in counter.values()))
    return pairs >= 98