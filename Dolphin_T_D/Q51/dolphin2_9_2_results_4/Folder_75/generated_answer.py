from collections import Counter

def if_contains_anagrams(strings):
    C = Counter()
    for s in strings:
        s = ''.join(filter(str.isalpha, s.lower()))
        if len(s) >= 3:
            C.update(s)
    pairs = 0
    for count in C.values():
        pairs += count * (count - 1) // 2
    return pairs <= 55