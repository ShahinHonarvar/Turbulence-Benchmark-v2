import itertools

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for word1, word2 in itertools.combinations(lst, 2):
        if len(word1) >= 3 and len(word2) >= 3 and (word1.lower() in [''.join(permutation) for permutation in itertools.permutations(word2.lower())]):
            anagram_pairs += 1
    if anagram_pairs >= 24:
        return True
    else:
        return False