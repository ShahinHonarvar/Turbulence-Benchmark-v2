from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    string_counts = Counter(normalized_strings)
    for value in string_counts.values():
        if value > 1:
            count += value * (value - 1) // 2
        if count > 60:
            return False
    return True