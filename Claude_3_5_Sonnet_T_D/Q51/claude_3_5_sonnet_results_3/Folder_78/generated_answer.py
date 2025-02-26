from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(str1, str2):
        if len(str1) < 3 or len(str2) < 3:
            return False
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    for str1, str2 in combinations(string_list, 2):
        filtered_str1 = ''.join((char for char in str1 if char.isalpha()))
        filtered_str2 = ''.join((char for char in str2 if char.isalpha()))
        if is_anagram(filtered_str1, filtered_str2):
            anagram_count += 1
            if anagram_count > 70:
                return False
    return True