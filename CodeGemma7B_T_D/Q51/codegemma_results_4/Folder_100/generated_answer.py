def if_contains_anagrams(str_list):
    if len(str_list) <= 1:
        return True
    str_list.sort(key=len)
    anagram_count = 0
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i].lower().strip()
            str2 = str_list[j].lower().strip()
            if sorted(str1) == sorted(str2):
                anagram_count += 1
                if anagram_count > 98:
                    return False
    return True