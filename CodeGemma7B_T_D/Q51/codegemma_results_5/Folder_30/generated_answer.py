def if_contains_anagrams(str_list):
    max_pairs = 28
    pairs_found = 0
    anagram_dict = {}
    for string in str_list:
        sort_string = ''.join(sorted(string.lower()))
        if sort_string not in anagram_dict:
            anagram_dict[sort_string] = string
        elif len(anagram_dict) <= max_pairs:
            pairs_found += 1
            del anagram_dict[sort_string]
    return pairs_found <= max_pairs