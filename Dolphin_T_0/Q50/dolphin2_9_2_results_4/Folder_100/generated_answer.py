def if_contains_anagrams(lst_of_strings):
    anagrams_count = 0
    for i in range(len(lst_of_strings)):
        for j in range(i + 1, len(lst_of_strings)):
            str_1 = lst_of_strings[i].lower()
            str_2 = lst_of_strings[j].lower()
            if len(str_1) >= 3 and len(str_2) >= 3 and (sorted(str_1) == sorted(str_2)):
                anagrams_count += 1
    return anagrams_count >= 95