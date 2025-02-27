def if_contains_anagrams(str_list):
    str_list.sort(key=len)
    anagrams = []
    for i in range(len(str_list) - 2):
        for j in range(i + 1, len(str_list) - 1):
            if sorted(str_list[i].lower()) == sorted(str_list[j].lower()):
                anagrams.append((str_list[i], str_list[j]))
    return len(anagrams) >= 21