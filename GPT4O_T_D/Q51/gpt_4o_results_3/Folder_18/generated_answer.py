from collections import defaultdict

def if_contains_anagrams(strings):
    normalized = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_chars = ''.join(sorted(s.lower()))
            normalized[sorted_chars] += 1
    count = 0
    for count_value in normalized.values():
        if count_value > 1:
            count += count_value * (count_value - 1) // 2
            if count > 42:
                return False
    return True