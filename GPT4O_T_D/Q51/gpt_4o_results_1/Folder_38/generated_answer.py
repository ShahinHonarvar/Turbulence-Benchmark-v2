from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted((c.lower() for c in s if c.isalpha())))
    anagram_map = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = sorted_chars(string)
            anagram_map[sorted_str] += 1
    total_pairs = sum((count * (count - 1) // 2 for count in anagram_map.values() if count > 1))
    return total_pairs <= 416