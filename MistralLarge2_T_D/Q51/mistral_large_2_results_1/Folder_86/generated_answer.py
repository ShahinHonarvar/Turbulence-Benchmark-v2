from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    anagram_pairs_count = 0
    for group in anagram_dict.values():
        if len(group) > 1:
            anagram_pairs_count += len(group) * (len(group) - 1) // 2
    return anagram_pairs_count <= 48