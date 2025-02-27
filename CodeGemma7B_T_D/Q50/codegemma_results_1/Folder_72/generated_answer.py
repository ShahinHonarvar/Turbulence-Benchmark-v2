def if_contains_anagrams(str_list):
    str_list_lower = [s.lower() for s in str_list]
    sorted_str_list_lower = [sorted(s) for s in str_list_lower]
    anagrams = {}
    num_anagrams = 0
    for s in sorted_str_list_lower:
        if s in anagrams:
            anagrams[s] += 1
        else:
            anagrams[s] = 1
        if anagrams[s] >= 55:
            num_anagrams += 1
    return num_anagrams >= 1