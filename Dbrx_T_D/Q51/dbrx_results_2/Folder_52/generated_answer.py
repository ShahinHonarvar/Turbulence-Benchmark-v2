from collections import defaultdict

def if_contains_anagrams(strings):
    all_anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        all_anagrams[sorted_string].append(string)
    pair_count = sum((1 for anagram_list in all_anagrams.values() if len(anagram_list) >= 2))
    return pair_count <= 43