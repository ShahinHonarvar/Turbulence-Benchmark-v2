import itertools

def palindromes_between_indices(s):
    """
    This function takes a string s and returns the set of all palindromes of the
    length of at least 3 such that each palindrome is formed from any possible
    arrangement of the English letters in the given string that occur between
    index 0 to index 4, both inclusive.
    """
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for p in itertools.permutations(s[:5], 3):
        if ''.join(p) == ''.join(p[::-1]):
            palindromes.add(''.join(p))
    return palindromes