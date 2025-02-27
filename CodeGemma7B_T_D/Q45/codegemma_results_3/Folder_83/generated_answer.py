from itertools import permutations
import string

def palindromes_between_indices(s):
    permutation_set = set()
    for permutation in permutations(s[2:10]):
        permutation_set.add(''.join(permutation))
    answer_set = set()
    for word in permutation_set:
        if word == word[::-1] and len(word) >= 7:
            answer_set.add(word.lower())
    return answer_set or set()