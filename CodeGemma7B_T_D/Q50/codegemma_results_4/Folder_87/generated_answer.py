def if_contains_anagrams(str_list):
    string_anagrams = {}
    size_str = 0
    for str in str_list:
        size_str += len(str)
        str = str.lower()
        sorted_str = ''.join(sorted(str))
        if sorted_str not in string_anagrams:
            string_anagrams[sorted_str] = 1
        else:
            string_anagrams[sorted_str] += 1
    num_anagrams = 0
    for strCount in string_anagrams.values():
        num_anagrams += strCount * (strCount - 1) // 2
    return num_anagrams >= 88