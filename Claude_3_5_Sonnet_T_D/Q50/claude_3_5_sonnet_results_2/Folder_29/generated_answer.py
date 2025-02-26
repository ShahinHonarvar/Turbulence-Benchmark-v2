from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    for word1, word2 in combinations(string_list, 2):
        if len(word1) >= 3 and len(word2) >= 3:
            if sorted(word1.lower()) == sorted(word2.lower()):
                anagram_count += 1
                if anagram_count >= 35:
                    return True
    return False