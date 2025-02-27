from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_dict[sorted_s].append(s)
    anagram_pairs_count = 0
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            anagram_pairs_count += len(anagram_list) * (len(anagram_list) - 1) // 2
            if anagram_pairs_count > 36:
                return False
    return True