def if_contains_anagrams(lst):
    anagrams_count = 0
    lst_length = len(lst)
    for i in range(lst_length):
        for j in range(i + 1, lst_length):
            str1 = sorted(lst[i].lower())
            str2 = sorted(lst[j].lower())
            if len(str1) >= 3 and len(str2) >= 3 and (str1 == str2):
                anagrams_count += 1
    return anagrams_count >= 60