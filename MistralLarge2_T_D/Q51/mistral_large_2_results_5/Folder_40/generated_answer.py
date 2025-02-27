from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_strings = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            sorted_strings[sorted_str] += 1
    anagram_pairs = sum((count // 2 for count in sorted_strings.values()))
    return anagram_pairs <= 29