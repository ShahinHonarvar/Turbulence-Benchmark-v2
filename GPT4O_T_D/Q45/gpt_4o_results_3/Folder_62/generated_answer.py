from itertools import permutations

def palindromes_between_indices(s):
    subsequence = ''.join(filter(str.isalpha, s[:9])).lower()
    unique_sub_palindromes = set()
    possible_permutations = set(permutations(subsequence))
    for perm in possible_permutations:
        candidate = ''.join(perm)
        if len(candidate) >= 7 and candidate == candidate[::-1]:
            unique_sub_palindromes.add(candidate)
    return unique_sub_palindromes