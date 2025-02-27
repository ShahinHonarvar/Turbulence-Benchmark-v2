from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    count = 0
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_dict[sorted_str].append(s)
    for anagrams in anagram_dict.values():
        count += len(anagrams) - 1
    return count <= 55