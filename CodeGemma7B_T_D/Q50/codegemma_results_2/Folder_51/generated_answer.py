def if_contains_anagrams(str_list):
    anagram_pairs = 0
    str_list.sort(key=len)
    str_list = [s.lower() for s in str_list]
    for i in range(len(str_list) - 2):
        for j in range(i + 2, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]) and len(str_list[i]) >= 3 and (len(str_list[j]) >= 3):
                anagram_pairs += 1
    return anagram_pairs >= 39