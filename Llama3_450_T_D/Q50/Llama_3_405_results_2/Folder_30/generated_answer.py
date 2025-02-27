from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3:
            anagrams[sorted_str].append(s)
    count = sum((len(val) * (len(val) - 1) // 2 for val in anagrams.values() if len(val) > 1))
    return count >= 78