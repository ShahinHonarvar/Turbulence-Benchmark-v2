from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for s in string_list:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s].append(s)
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        if n > 1:
            anagram_count += n * (n - 1) // 2
    return anagram_count >= 177