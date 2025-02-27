from collections import Counter
    from itertools import permutations

def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for word in list_of_strings:
        if len(word) >= 3:
            sorted_word = sorted(word.lower())
            for perm in permutations(sorted_word):
                if ''.join(perm) != word.lower():
                    if Counter(''.join(perm)) == Counter(word.lower()):
                        anagram_pairs += 1
    return anagram_pairs >= 26