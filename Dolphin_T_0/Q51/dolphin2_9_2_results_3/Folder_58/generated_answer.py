from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    for word1 in lst:
        for word2 in lst:
            if len(word1) >= 3 and len(word2) >= 3 and is_anagram(word1, word2) and (word1 != word2):
                count += 1
                break
        if count > 60:
            return False
    return True