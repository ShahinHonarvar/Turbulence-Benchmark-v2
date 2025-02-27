def if_contains_anagrams(str_list):
    anagrams = {}
    for str in str_list:
        str_lower = str.lower()
        sorted_str = ''.join(sorted(str_lower))
        if sorted_str in anagrams:
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    return sum((value for value in anagrams.values())) <= 79