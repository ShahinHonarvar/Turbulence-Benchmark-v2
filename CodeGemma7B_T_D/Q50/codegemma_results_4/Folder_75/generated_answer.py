from itertools import permutations

def count_anagrams(str_list):
    anagram_count = 0
    for string in str_list:
        for other_string in str_list:
            if string != other_string and sorted(string.lower()) == sorted(other_string.lower()):
                anagram_count += 1
    return anagram_count

def if_contains_anagrams(str_list):
    anagram_count = count_anagrams(str_list)
    return anagram_count >= 70