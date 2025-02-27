from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagram_dict[sorted_s].append(s)
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 177