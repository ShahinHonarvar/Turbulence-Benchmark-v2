def if_contains_anagrams(lst):
    anagram_count = 0
    lst_len = len(lst)
    for i in range(lst_len):
        for j in range(i + 1, lst_len):
            str1 = sorted(lst[i].lower())
            str2 = sorted(lst[j].lower())
            if len(str1) >= 3 and len(str2) >= 3 and (str1 == str2):
                anagram_count += 1
    return anagram_count >= 59