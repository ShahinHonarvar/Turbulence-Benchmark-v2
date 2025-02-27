def if_contains_anagrams(str_list):
    anagram_count = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str_i = str_list[i]
            str_j = str_list[j]
            if len(str_i) < 3 or len(str_j) < 3:
                continue
            str_i = str_i.lower()
            str_j = str_j.lower()
            if sorted(str_i) == sorted(str_j):
                anagram_count += 1
    return anagram_count >= 17