from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[sorted_str].append(s)
    count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1))
    return count >= 30