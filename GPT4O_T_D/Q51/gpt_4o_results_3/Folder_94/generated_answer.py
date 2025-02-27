from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    strings = [s.lower() for s in strings]
    seen = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            signature = ''.join(sorted(s))
            seen[signature] += 1
    for value in seen.values():
        if value > 1:
            count += value * (value - 1) // 2
            if count > 181:
                return False
    return True