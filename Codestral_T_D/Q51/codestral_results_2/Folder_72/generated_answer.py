from collections import Counter

def if_contains_anagrams(lst):
    count = Counter()
    for word in lst:
        if len(word) >= 3:
            count[frozenset(Counter(word.lower()))] += 1
    return sum((v * (v - 1) // 2 for v in count.values())) <= 188