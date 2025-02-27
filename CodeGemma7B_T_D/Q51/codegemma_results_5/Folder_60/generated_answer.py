def if_contains_anagrams(str_list):

    def is_anagram(str1, str2):
        if len(str1) != len(str2):
            return False
        str1 = sorted(str1.lower())
        str2 = sorted(str2.lower())
        return str1 == str2
    anagram_pairs = set()
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i]
            str2 = str_list[j]
            if is_anagram(str1, str2) and len(str1) >= 3:
                anagram_pairs.add((str1, str2))
    return len(anagram_pairs) <= 77