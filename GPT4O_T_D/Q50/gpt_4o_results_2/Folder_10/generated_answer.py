from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sort_string(s)
            anagram_count += anagram_dict[sorted_s]
            anagram_dict[sorted_s] += 1
    return anagram_count >= 52