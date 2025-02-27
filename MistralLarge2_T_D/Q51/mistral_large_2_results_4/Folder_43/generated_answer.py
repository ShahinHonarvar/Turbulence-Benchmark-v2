from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagram_dict[sorted_s].append(s)
    anagram_pairs = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            pairs = len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
            anagram_pairs += pairs
            if anagram_pairs > 3:
                return False
    return True