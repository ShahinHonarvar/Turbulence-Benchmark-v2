from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    anagram_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            anagram_map[sorted_string(s)] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_map.values()))
    return anagram_pairs <= 57