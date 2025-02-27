from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_pairs_count = 0
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagram_dict[key].append(s)
    for key, anagrams in anagram_dict.items():
        if len(anagrams) > 1:
            anagram_pairs_count += len(anagrams) - 1
    return anagram_pairs_count <= 17