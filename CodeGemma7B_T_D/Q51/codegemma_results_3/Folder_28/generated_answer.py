def if_contains_anagrams(str_list):
    anagram_pairs = set()
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3 and (str_list[i].lower() == str_list[j].lower()):
                anagram_pairs.add((str_list[i], str_list[j]))
    return len(anagram_pairs) <= 78