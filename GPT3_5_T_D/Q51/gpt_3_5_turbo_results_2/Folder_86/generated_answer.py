import itertools

def if_contains_anagrams(lst):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    count = 0
    for word1, word2 in itertools.combinations(lst, 2):
        if is_anagram(word1, word2) and len(word1) >= 3:
            count += 1
            if count > 48:
                return False
    return True