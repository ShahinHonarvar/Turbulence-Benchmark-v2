from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    count = 0
    lower_strings = [s.lower() for s in strings]
    for s in lower_strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            anagram_count[sorted_str] += 1
    for value in anagram_count.values():
        if value > 1:
            count += value * (value - 1) // 2
            if count > 147:
                return False
    return True