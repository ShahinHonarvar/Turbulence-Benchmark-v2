from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            counter[sorted_word] += 1
    num_anagrams = sum((v * (v - 1) // 2 for v in counter.values() if v > 1))
    return num_anagrams <= 407