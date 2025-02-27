def if_contains_anagrams(str_list):
    anagram_pairs = set()
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            s1, s2 = (str_list[i].lower(), str_list[j].lower())
            if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2)):
                anagram_pairs.add((s1, s2))
    return len(anagram_pairs) <= 86