from itertools import permutations

def palindromes_between_indices(text):
    """
    This function takes a string as input and returns the set of all palindromes of the length of at least 5 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 3 to index 8, both inclusive.
    """
    text = text[4:9].lower()
    result = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            palindrome = ''.join(sorted(text[i:j]))
            result.add(palindrome)
    if not result:
        return set()