from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for string in strings:
        if len(string) >= 3:
            counter[frozenset(Counter(string.lower()))] += 1
    return sum((count * (count - 1) // 2 for count in counter.values())) >= 15