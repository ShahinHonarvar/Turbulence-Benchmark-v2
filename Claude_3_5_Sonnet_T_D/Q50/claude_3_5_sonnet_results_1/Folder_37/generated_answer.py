from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s].append(s)
    anagram_pairs = 0
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        anagram_pairs += n * (n - 1) // 2
        if anagram_pairs >= 29:
            return True
    return False