def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            anagrams.setdefault(sorted_str, []).append(string)
    return len(anagrams) >= 39