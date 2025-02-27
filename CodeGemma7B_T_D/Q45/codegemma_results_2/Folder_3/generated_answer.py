from itertools import product

def palindromes_between_indices(s):
    """
            Returns the set of palindromes of the length of at least 3 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 7 to index 9, both inclusive.

            Args:
                s: The given string.

            Returns:
                The set of palindromes of the length of at least 3.
            """
    letters = ''.join(filter(str.isalpha, s[7:10].lower()))
    palindromes = set()
    for p in product(letters, repeat=len(letters)):
        if ''.join(p) == ''.join(p[::-1]):
            palindromes.add(''.join(p))
    return palindromes