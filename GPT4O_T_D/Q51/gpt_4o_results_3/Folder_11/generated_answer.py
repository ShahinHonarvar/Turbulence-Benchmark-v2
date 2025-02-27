from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted((c for c in s.lower() if c.isalpha())))
    anagram_groups = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = sorted_chars(s)
            anagram_groups[key] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_groups.values()))
    return anagram_pairs <= 41