from collections import Counter
from itertools import combinations

def if_contains_anagrams(list_of_strings):
    count = 0
    for word1, word2 in combinations(list_of_strings, 2):
        lowercase_word1 = word1.lower()
        lowercase_word2 = word2.lower()
        if len(lowercase_word1) >= 3 and len(lowercase_word2) >= 3:
            sorted_word1 = ''.join(sorted(lowercase_word1))
            sorted_word2 = ''.join(sorted(lowercase_word2))
            if sorted_word1 == sorted_word2:
                count += 1
    return count <= 181