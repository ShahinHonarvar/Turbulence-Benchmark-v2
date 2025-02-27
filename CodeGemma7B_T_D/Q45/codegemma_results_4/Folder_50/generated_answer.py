def palindromes_between_indices(s):
    """
  This function takes a string and returns the set of all palindromes of the length of at least 5
  such that each palindrome is created from any possible arrangement of the English letters in
  the given string that occur between index 4 to index 8, both inclusive.
  """
    letters = sorted([c.lower() for c in s[4:9] if c.isalpha()])
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm)
        palindromes.add(palindrome)
    return palindromes