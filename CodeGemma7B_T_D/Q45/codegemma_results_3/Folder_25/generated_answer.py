def palindromes_between_indices(text):
    """
    Returns the set of all palindromes of the length of at least 3 such that each palindrome is created from any
    possible arrangement of the English letters in the given string that occur between index 1 to index 4, both inclusive.
    """
    if not text[1:5].casefold():
        return set()
    palindromes = set()
    for word in permutations(text[1:5]):
        if word[0] not in 'AEIOUaeiou':
            palindromes.add(''.join(word))
    return palindromes