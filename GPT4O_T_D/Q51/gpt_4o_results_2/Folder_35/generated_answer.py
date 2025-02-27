from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    lowercase_strings = [s.lower() for s in strings]
    for string in lowercase_strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string))
            anagram_map[sorted_str] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_map.values() if count > 1))
    return anagram_pairs <= 210