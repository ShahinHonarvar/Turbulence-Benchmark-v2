from itertools import permutations

def palindromes_between_indices(s):
    """
    This function takes one argument, which is a string. 
    It returns the set of all palindromes of the length of at least 5 such that each palindrome is created from any possible 
    arrangement of the English letters in the given string that occur between index 1 to index 5, both inclusive. If no 
    such palindromes of the specified length can be created from the English letters of the given string that occur in the 
    specified range, the function should return an empty set.
    """
    palindromes = set()
    if len(s) < 5:
        return palindromes
    word = ''.join([c.lower() for c in s[1:6] if c.isalpha()])
    for permutation in permutations(word):
        if permutation == permutation[::-1]:
            palindromes.add(''.join(permutation))
    return palindromes