def if_contains_anagrams(str_list):
    seen_anagrams = set()
    seen_str_len = set()
    for string in str_list:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if len(string) >= 3 and sorted_string not in seen_anagrams:
            seen_anagrams.add(sorted_string)
            seen_str_len.add(len(string))
    return len(seen_anagrams) >= 54 and len(seen_str_len) >= 43