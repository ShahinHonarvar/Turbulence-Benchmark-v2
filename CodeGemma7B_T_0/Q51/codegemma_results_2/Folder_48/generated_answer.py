def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) < 3:
            continue
        if sorted_str not in anagram_dict:
            anagram_dict[sorted_str] = []
        anagram_dict[sorted_str].append(string)
    return len(anagram_dict) <= 277