def if_contains_anagrams(str_list):

    def is_anagram(str1, str2):
        str1, str2 = (str1.lower(), str2.lower())
        return sorted(str1) == sorted(str2) and len(str1) >= 3
    pairs = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]):
                pairs += 1
    return pairs >= 14