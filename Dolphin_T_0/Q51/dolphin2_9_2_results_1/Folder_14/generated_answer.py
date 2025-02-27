from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            counter[sorted_string] += 1
    return any((v > 1 for v in counter.values()))