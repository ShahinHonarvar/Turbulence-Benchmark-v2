from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return len(s1) >= 3 and sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = sum((1 for s1, s2 in combinations(string_list, 2) if is_anagram(s1, s2)))
    return anagram_count >= 411