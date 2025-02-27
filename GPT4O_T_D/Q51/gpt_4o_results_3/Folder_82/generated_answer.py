from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    anagram_dict = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_dict[sorted_s].append(s.lower())
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        if n > 1:
            count += n * (n - 1) // 2
            if count > 40:
                return False
    return count <= 40