from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for word1 in lst:
        if len(word1) >= 3:
            for word2 in lst:
                if len(word2) >= 3 and word1 != word2 and (Counter(word1.lower()) == Counter(word2.lower())):
                    anagram_pairs += 1
    return anagram_pairs >= 20