from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3 and sorted_s.isalpha():
            anagrams[sorted_s].append(s)
    count = sum((len(values) * (len(values) - 1) // 2 for values in anagrams.values() if len(values) > 1))
    return count <= 42