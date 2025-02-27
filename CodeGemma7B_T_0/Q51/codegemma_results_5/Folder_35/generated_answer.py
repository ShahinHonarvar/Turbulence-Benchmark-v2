def if_contains_anagrams(str_list):
    anagram_count = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i].lower()
            str2 = str_list[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2)):
                anagram_count += 1
    return anagram_count <= 210