from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        s1 = ''.join(filter(str.isalpha, s1.lower()))
        s2 = ''.join(filter(str.isalpha, s2.lower()))
        return len(s1) >= 3 and sorted(s1) == sorted(s2)
    anagram_count = 0
    for s1, s2 in combinations(string_list, 2):
        if is_anagram(s1, s2):
            anagram_count += 1
            if anagram_count > 46:
                return False
    return True