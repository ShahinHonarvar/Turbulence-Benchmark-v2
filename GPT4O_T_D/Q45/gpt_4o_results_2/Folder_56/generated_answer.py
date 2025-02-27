from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:10]
    letters = [ch.lower() for ch in substring if ch.isalpha()]
    result_set = set()
    for p in permutations(letters):
        permuted_string = ''.join(p)
        if len(permuted_string) >= 5 and permuted_string == permuted_string[::-1]:
            result_set.add(permuted_string)
    return result_set