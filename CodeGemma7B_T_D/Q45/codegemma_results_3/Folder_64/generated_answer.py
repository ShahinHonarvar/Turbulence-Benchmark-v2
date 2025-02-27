from itertools import permutations

def palindromes_between_indices(word):
    """
  This function takes one argument, which is a string, and returns the set of
  all palindromes of the length of at least 5 such that each palindrome is
  created from any possible arrangement of the English letters in the given
  string that occur between index 4 to index 9, both inclusive. If no such
  palindromes of the specified length can be created from the English
  letters of the given string that occur in the specified range, the
  function should return an empty set. The function should form each
  palindrome in a case-insensitive manner.
  """
    letters = ''.join(sorted([char.upper() for char in word[4:10]]))
    permutations_list = permutations(letters)
    palindromes = {''.join(perm) for perm in permutations_list if perm == perm[::-1]}
    return {palindrome for palindrome in palindromes if len(palindrome) >= 5}