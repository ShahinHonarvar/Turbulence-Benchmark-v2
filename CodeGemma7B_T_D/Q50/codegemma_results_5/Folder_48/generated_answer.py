def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=lambda s: len(s))
    num_anagrams = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) != len(str_list[j]):
                continue
            if sorted(str_list[i]) == sorted(str_list[j]):
                num_anagrams += 1
    return num_anagrams >= 219