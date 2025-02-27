def if_contains_anagrams(str_list):
    str_list.sort(key=len)
    str_list = [s.lower() for s in str_list]
    anagram_pairs = set()
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]) and len(str_list[i]) >= 3 and (len(str_list[j]) >= 3):
                anagram_pairs.add((tuple(sorted(str_list[i])), tuple(sorted(str_list[j]))))
    return len(anagram_pairs) >= 52