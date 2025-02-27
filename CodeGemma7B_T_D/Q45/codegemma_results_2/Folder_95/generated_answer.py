from collections import Counter

def palindromes_between_indices(string):
    """
            Returns the set of all palindromes of the length of at least 3 such that
            each palindrome is created from any possible arrangement of the English
            letters in the given string that occur between index 7 to index 8, both inclusive.

            If no such palindromes of the specified length can be created from the
            English letters of the given string that occur in the specified range,
            the function should return an empty set.

            The function should form each palindrome in a case-insensitive manner.
            """
    letters = [char.lower() for char in string[7:9] if char.isalpha()]
    counts = Counter(letters)
    if not counts:
        return set()
    palindromes = set()
    for perm in itertools.product(*map(counts.values, counts)):
        palindrome = ''.join(itertools.chain.from_iterable(zip(letters, perm)))
        if len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes