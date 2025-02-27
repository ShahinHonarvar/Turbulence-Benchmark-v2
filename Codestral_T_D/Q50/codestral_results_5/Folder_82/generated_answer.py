from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sort_string(s)
            anagram_dict[sorted_s].append(s)
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            pairs = len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
            if pairs >= 276:
                return True
    return False