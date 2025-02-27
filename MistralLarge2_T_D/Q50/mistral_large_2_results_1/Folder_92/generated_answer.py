from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string].append(string)
    count_pairs = sum((1 for key in anagram_dict if len(anagram_dict[key]) >= 2))
    return count_pairs >= 2