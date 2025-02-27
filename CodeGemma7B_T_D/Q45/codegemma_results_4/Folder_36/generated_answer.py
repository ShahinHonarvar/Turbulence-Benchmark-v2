def palindromes_between_indices(text):
    """
  Finds the set of palindromes with length >= 3 formed from the substring of the given
  string from index 5 to index 8 (inclusive). A palindrome is case-insensitive.

  Args:
    text: The input string.

  Returns:
    The set of palindromes that satisfy the conditions, or an empty set if no such
    palindromes exist.
  """
    substring = text[5:9].lower()
    permutations = list((''.join(p) for p in itertools.permutations(substring)))
    palindromes = [p for p in permutations if p == p[::-1] and len(p) >= 3]
    return set(palindromes)