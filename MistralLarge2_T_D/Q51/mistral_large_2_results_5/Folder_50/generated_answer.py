from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_dict[sorted_str].append(s)
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            anagram_pairs = len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
            anagram_count += anagram_pairs
    return anagram_count <= 47