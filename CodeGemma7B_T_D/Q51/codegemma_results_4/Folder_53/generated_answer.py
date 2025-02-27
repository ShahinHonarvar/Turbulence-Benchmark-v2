from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_pairs = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_pairs[sorted_string].append(string)
    return len(anagram_pairs) <= 8