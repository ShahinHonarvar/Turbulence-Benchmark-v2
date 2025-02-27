from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_dict[sorted_str].append(s)
    anagram_pairs_count = sum((1 for anagrams in anagram_dict.values() if len(anagrams) > 1))
    return anagram_pairs_count <= 11