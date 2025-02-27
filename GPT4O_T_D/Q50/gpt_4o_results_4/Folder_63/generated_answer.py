from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            sorted_anagram = sorted_chars(s)
            anagram_count += anagram_dict[sorted_anagram]
            anagram_dict[sorted_anagram] += 1
    return anagram_count >= 89