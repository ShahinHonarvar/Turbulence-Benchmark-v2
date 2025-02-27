def if_contains_anagrams(str_list):
    anagram_pairs = 0
    str_dict = {}
    for string in str_list:
        string = ''.join(sorted(string.lower()))
        if string in str_dict:
            anagram_pairs += 1
        else:
            str_dict[string] = True
    return anagram_pairs <= 28