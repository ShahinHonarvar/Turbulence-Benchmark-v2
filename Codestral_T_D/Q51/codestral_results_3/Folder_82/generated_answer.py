from collections import Counter

def if_contains_anagrams(strings):
    count = Counter([''.join(sorted(s.lower())) for s in strings if len(s) >= 3])
    return sum((n * (n - 1) // 2 for n in count.values())) <= 40