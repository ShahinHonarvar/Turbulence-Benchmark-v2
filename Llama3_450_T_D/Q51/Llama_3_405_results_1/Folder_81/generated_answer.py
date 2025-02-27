def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for s in string_list:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_string = ''.join(sorted(s))
        if sorted_string in anagram_dict:
            anagram_count += anagram_dict[sorted_string]
            anagram_dict[sorted_string] += 1
        else:
            anagram_dict[sorted_string] = 1
    return anagram_count <= 79