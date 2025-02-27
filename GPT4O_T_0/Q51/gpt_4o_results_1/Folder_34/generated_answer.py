from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_dict[sorted_s].append(s)
    for anagram_list in anagram_dict.values():
        n = len(anagram_list)
        if n > 1:
            anagram_count += n * (n - 1) // 2
            if anagram_count > 401:
                return False
    return True