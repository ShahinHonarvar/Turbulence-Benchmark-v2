def if_contains_anagrams(str_list):
    anagram_pairs = 0
    str_list = [str.lower() for str in str_list]
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if str_list[i] != str_list[j] and sorted(str_list[i]) == sorted(str_list[j]):
                anagram_pairs += 1
    return anagram_pairs >= 50