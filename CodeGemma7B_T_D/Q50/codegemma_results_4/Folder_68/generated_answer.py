from itertools import combinations

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [s for length in range(3, 10) for s in str_list if len(s) == length]
    str_list.sort()
    anagram_count = 0
    for i in range(len(str_list) - 2):
        for j in range(i + 2, len(str_list)):
            if set(str_list[i]) == set(str_list[j]):
                anagram_count += 1
    return anagram_count >= 9