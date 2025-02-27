def if_contains_anagrams(str_list):
    anagram_pairs = []
    for i, str1 in enumerate(str_list):
        for j in range(i + 1, len(str_list)):
            str2 = str_list[j]
            if sorted(str1.lower()) == sorted(str2.lower()) and len(str1) >= 3 and (len(str2) >= 3) and (str1 != str2):
                anagram_pairs.append((str1, str2))
    return len(anagram_pairs) <= 25