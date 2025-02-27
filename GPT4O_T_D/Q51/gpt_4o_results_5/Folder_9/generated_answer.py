from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_chars(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    anagram_map = defaultdict(int)
    for string in lst:
        if len(string) >= 3:
            sorted_str = sorted_chars(string)
            anagram_map[sorted_str] += 1
    anagram_pairs_count = sum((count * (count - 1) // 2 for count in anagram_map.values()))
    return anagram_pairs_count <= 475