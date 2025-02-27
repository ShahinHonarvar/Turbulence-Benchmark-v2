from itertools import combinations

def if_contains_anagrams(str_list):
    str_list = [x.lower() for x in str_list if len(x) >= 3]
    pairs = list(combinations(str_list, 2))

    def are_anagrams(str1, str2):
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)
        return sorted_str1 == sorted_str2
    anagrams = [pair for pair in pairs if are_anagrams(*pair)]
    return len(anagrams) >= 246