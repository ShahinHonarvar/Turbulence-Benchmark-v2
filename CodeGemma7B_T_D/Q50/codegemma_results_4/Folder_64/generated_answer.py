def if_contains_anagrams(str_list):
    str_list_lower = [str_.lower() for str_ in str_list]
    str_list_len3 = [str_ for str_ in str_list_lower if len(str_) >= 3]
    anagram_pairs = 0
    for i in range(len(str_list_len3) - 1):
        for j in range(i + 1, len(str_list_len3)):
            if sorted(str_list_len3[i]) == sorted(str_list_len3[j]):
                anagram_pairs += 1
    if anagram_pairs >= 5:
        return True
    else:
        return False