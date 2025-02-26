from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    for s1, s2 in combinations(string_list, 2):
        s1_filtered = ''.join(filter(str.isalpha, s1))
        s2_filtered = ''.join(filter(str.isalpha, s2))
        if len(s1_filtered) >= 3 and len(s2_filtered) >= 3:
            if is_anagram(s1_filtered, s2_filtered):
                anagram_count += 1
                if anagram_count > 276:
                    return False
    return True