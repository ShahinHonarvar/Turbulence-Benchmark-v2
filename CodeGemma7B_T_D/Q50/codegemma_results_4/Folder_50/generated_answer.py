def if_contains_anagrams(str_list):
    anagram_pairs = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i].lower()
            str2 = str_list[j].lower()
            str1_sorted = sorted(str1)
            str2_sorted = sorted(str2)
            if str1_sorted == str2_sorted and len(str1) >= 3 and (len(str2) >= 3):
                anagram_pairs += 1
    return anagram_pairs >= 20