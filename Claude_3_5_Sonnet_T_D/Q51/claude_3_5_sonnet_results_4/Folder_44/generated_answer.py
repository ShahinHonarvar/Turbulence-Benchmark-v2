from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return len(s1) >= 3 and sorted(s1.lower()) == sorted(s2.lower())
    cleaned_list = [''.join(filter(str.isalpha, s)) for s in string_list]
    anagram_pairs = sum((1 for s1, s2 in combinations(cleaned_list, 2) if is_anagram(s1, s2)))
    return anagram_pairs <= 75