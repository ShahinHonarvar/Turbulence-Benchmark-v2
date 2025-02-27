import itertools

def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for word1, word2 in itertools.combinations(string_list, 2):
        if len(word1) >= 3 and len(word2) >= 3 and (sorted(word1.lower()) == sorted(word2.lower())):
            anagram_pairs += 1
            if anagram_pairs >= 42:
                return True
    return False