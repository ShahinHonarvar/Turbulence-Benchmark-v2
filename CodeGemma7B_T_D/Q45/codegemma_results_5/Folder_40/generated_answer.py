from itertools import permutations

def palindromes_between_indices(text):
    """
    This function takes a string as input and returns the set of all palindromes of the length of at least 7 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 4 to index 9, both inclusive.
    """
    palindrome = {''.join(p) for p in permutations(text[4:10].lower()) if len(p) >= 7}
    if len(palindrome) == 0:
        return set()
    return palindrome