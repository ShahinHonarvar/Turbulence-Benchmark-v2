from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_dict[sorted_str].append(s)
    anagram_count = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) >= 2:
            anagram_count += 1
    return anagram_count >= 233