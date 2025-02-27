def if_contains_anagrams(str_list):
    str_list.sort(key=len)
    anagrams = []
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]):
                anagrams.append((str_list[i], str_list[j]))
    return len(anagrams) <= 423