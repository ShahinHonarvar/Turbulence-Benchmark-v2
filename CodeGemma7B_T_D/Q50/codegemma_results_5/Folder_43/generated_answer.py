def if_contains_anagrams(str_list):
    anagram_pairs = 0
    str_list_lower = [word.lower() for word in str_list]
    for i in range(len(str_list_lower)):
        for j in range(i + 1, len(str_list_lower)):
            if sorted(str_list_lower[i]) == sorted(str_list_lower[j]) and len(str_list_lower[i]) >= 3 and (len(str_list_lower[j]) >= 3):
                anagram_pairs += 1
    return anagram_pairs >= 61