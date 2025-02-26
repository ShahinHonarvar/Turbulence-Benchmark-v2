from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    filtered_list = [''.join(filter(str.isalpha, s.lower())) for s in string_list]
    filtered_list = [s for s in filtered_list if len(s) >= 3]
    for s1, s2 in combinations(filtered_list, 2):
        if sorted(s1) == sorted(s2):
            anagram_count += 1
            if anagram_count > 475:
                return False
    return True