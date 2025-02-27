from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for string in strings:
        counter[tuple(sorted(string.lower()))] += 1
    return sum((count * (count - 1) // 2 for count in counter.values())) <= 416