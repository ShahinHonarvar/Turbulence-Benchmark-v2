from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    for str1, str2 in combinations(string_list, 2):
        str1_filtered = ''.join(filter(str.isalpha, str1))
        str2_filtered = ''.join(filter(str.isalpha, str2))
        if len(str1_filtered) >= 3 and len(str2_filtered) >= 3:
            if is_anagram(str1_filtered, str2_filtered):
                anagram_count += 1
                if anagram_count > 74:
                    return False
    return True