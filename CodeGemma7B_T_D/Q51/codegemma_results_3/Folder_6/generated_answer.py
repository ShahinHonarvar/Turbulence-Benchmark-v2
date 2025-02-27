def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    str_list = [str for str in str_list if len(str) >= 3]
    anagrams = {}
    for str in str_list:
        sorted_str = ''.join(sorted(str))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = [str]
        else:
            anagrams[sorted_str].append(str)
    return len(anagrams) <= 86