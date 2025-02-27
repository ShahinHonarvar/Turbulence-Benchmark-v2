from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_characters(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = sort_characters(s)
            anagram_dict[sorted_str] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values() if v > 1))
    return anagram_pairs >= 219