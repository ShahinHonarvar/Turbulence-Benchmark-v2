from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for word1 in lst:
        for word2 in lst:
            if len(word1) >= 3 and len(word2) >= 3 and (word1.lower() != word2.lower()):
                if Counter(word1.lower()) == Counter(word2.lower()):
                    anagram_pairs += 1
    if anagram_pairs <= 65:
        return True
    else:
        return False