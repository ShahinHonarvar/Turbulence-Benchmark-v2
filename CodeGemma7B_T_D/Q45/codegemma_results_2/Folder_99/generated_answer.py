from itertools import permutations

def palindromes_between_indices(text):
    """
  Write a function called 'palindromes_between_indices' that takes one argument,
  which is a string. The given string may consist of any character. The
  function should return the set of all palindromes of the length of at least 3
  such that each palindrome is created from any possible arrangement of the
  English letters in the given string that occur between index 4 to index 8, both inclusive.
  If no such palindromes of the specified length can be created from the English letters
  of the given string that occur in the specified range, the function should return an empty set.
  The function should form each palindrome in a case-insensitive manner.
  """
    text = text.lower()
    letters = list(text[4:9])
    palindromes = set()
    for letters in permutations(letters):
        palindrome = ''.join(letters)
        if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes