from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_strings = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_strings[''.join(sorted(s.lower()))] += 1
    total_pairs = sum((x * (x - 1) // 2 for x in sorted_strings.values()))
    return total_pairs >= 19