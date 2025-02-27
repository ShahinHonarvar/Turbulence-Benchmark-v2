def if_contains_anagrams(str_list):
    str_list = sorted(str_list, key=len)
    anagram_pairs = 0
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            str1 = ''.join(sorted(str_list[i].lower()))
            str2 = ''.join(sorted(str_list[j].lower()))
            if str1 == str2:
                anagram_pairs += 1
    return anagram_pairs <= 85