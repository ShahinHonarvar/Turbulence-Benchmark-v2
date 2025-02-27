def if_contains_anagrams(data_list):
    anagram_pairs = 0
    for i in range(len(data_list) - 1):
        for j in range(i + 1, len(data_list)):
            str1 = data_list[i].lower()
            str2 = data_list[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2)):
                anagram_pairs += 1
    if anagram_pairs >= 58:
        return True
    else:
        return False