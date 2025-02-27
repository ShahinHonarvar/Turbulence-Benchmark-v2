import itertools

def palindromes_between_indices(text):
    """
    Finds the set of all palindromes of the length of at least 5
    such that each palindrome is created from any possible arrangement
    of the English letters in the given string that occur between
    index 4 to index 8, both inclusive.
    """
    eight_letter_substring = text[4:9]
    eight_letter_substring = eight_letter_substring.lower()

    def is_palindrome(word):
        """
        Checks if a given string is a palindrome.
        """
        return word == word[::-1]
    palindromes = set()
    for permutation in itertools.permutations(eight_letter_substring):
        permutation = ''.join(permutation)
        if is_palindrome(permutation):
            palindromes.add(permutation)
    return palindromes