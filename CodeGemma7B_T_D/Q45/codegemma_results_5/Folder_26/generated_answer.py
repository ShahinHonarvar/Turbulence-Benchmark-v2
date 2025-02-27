def palindromes_between_indices(text):
    """
    Returns the set of all palindromes of the length of at least 3 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 4 to index 6, both inclusive. If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set. The function should form each palindrome in a case-insensitive manner.
    """
    text = text.lower()
    letters = text[4:7]
    if len(set(letters)) < 2:
        return set()
    permutations = itertools.permutations(letters)
    palindromes = set()
    for permutation in permutations:
        palindrome = ''.join(permutation)
        palindromes.add(palindrome)
    palindromes = {palindrome for palindrome in palindromes if len(palindrome) >= 3}
    return palindromes