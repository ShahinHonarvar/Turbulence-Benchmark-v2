from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    processed_strings = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            normalized = ''.join(sorted(s.lower()))
            processed_strings[normalized] += 1
    for value in processed_strings.values():
        if value > 1:
            count += value * (value - 1) // 2
            if count > 85:
                return False
    return True