from itertools import permutations

def if_contains_anagrams(str_list):
    str_list = [word.lower() for word in str_list]
    str_list = sorted(str_list, key=len)
    anagram_pairs = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3 and (str_list[i] != str_list[j]):
                if sorted(str_list[i]) == sorted(str_list[j]):
                    anagram_pairs += 1
    return anagram_pairs >= 68