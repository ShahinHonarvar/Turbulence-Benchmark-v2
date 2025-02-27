from collections import Counter

def if_contains_anagrams(strings):
    strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    count = 0
    for key, value in Counter(strings).items():
        if value > 1:
            count += value * (value - 1) // 2
    return count <= 318