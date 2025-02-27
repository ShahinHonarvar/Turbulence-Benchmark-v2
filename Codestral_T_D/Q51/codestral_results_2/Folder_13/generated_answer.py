from collections import Counter

def if_contains_anagrams(strings):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    count = Counter()
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted((c for c in s.lower() if c in letters)))
            count[key] += 1
    return sum((v * (v - 1) // 2 for v in count.values())) <= 54