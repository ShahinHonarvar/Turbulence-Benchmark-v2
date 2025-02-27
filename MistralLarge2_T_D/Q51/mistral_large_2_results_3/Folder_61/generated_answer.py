from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_dict[sorted_s].append(s)
    anagram_pairs = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            anagram_pairs += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_pairs <= 50