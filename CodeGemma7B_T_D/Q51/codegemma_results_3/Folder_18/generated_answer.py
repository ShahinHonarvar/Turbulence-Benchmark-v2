from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3 or not sorted_string.isalpha():
            continue
        anagram_dict[sorted_string].append(string)
    count = sum((len(anagrams) >= 2 for anagrams in anagram_dict.values()))
    return count <= 42