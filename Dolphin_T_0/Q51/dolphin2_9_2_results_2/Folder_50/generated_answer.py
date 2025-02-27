import itertools

def if_contains_anagrams(string_list):
    count_anagrams = 0
    for word1 in string_list:
        if len(word1) >= 3:
            for word2 in string_list:
                if len(word2) >= 3:
                    if sorted(word1.lower()) == sorted(word2.lower()):
                        count_anagrams += 1
    return count_anagrams // 2 <= 47