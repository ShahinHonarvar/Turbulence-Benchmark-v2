from itertools import permutations

def palindromes_between_indices(s):
    """
    Returns set of all palindromes of length 4+ such that
    each palindrome is created from any possible arrangement of the
    English letters in the given string that occur between
    index 3 to index 7, inclusive.
    """
    palindromes = set()
    for perm in permutations(s[3:8].lower()):
        if perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return palindromes