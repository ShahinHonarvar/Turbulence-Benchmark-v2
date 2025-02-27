def if_contains_anagrams(string_list):
    anagram_pairs = set()
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            str1 = string_list[i].lower()
            str2 = string_list[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and (str1 != str2) and (sorted(str1) == sorted(str2)):
                anagram_pairs.add((str1, str2))
    return len(anagram_pairs) <= 147