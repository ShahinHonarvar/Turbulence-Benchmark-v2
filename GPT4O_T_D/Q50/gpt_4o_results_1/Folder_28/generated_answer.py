from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_tuple = tuple(sorted(s.lower()))
            anagram_dict[sorted_tuple].append(s)
    count = 0
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        if n > 1:
            count += n * (n - 1) // 2
            if count >= 81:
                return True
    return False