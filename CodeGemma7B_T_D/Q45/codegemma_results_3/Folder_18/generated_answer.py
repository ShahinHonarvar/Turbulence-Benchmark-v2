from itertools import permutations

def palindromes_between_indices(string):
    """
  Returns the set of all palindromes of the length of at least 3 such that each palindrome
  is created from any possible arrangement of the English letters in the given string that
  occur between index 1 to index 6, both inclusive. If no such palindromes of the
  specified length can be created from the English letters of the given string that
  occur in the specified range, the function should return an empty set. The function
  should form each palindrome in a case-insensitive manner.
  """
    letters = [c.lower() for c in string][0:6]
    if len(letters) < 3:
        return set()
    arrangements = permutations(letters)
    palindromes = set()
    for arrangement in arrangements:
        if arrangement[0] == arrangement[-1]:
            palindromes.add(''.join(arrangement))
    return palindromes