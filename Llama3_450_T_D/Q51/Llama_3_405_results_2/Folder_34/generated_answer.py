from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            sorted_s = ''.join(sorted(s.lower()))
            anagrams[sorted_s].append(s)
    count = sum((len(vals) * (len(vals) - 1) // 2 for vals in anagrams.values()))
    return count <= 401