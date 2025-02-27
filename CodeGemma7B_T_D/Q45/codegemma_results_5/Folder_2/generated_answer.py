def palindromes_between_indices(word):
    """
  Creates a set of all palindromes of length at least 6
  such that each palindrome is created from any possible
  arrangement of the English letters in the given string that
  occur between index 1 to index 5, both inclusive.

  Args:
    word: The string to create palindromes from.

  Returns:
    A set of palindromes of length at least 6 or an
    empty set if no palindromes can be created.
  """
    if not word[1:6]:
        return set()
    word = word.lower()
    palindromes = set()
    for i in range(5):
        for j in range(i + 1, 6):
            for k in range(j + 1, 7):
                for m in range(k + 1, 8):
                    for n in range(m + 1, 9):
                        palindrome = word[i] + word[j] + word[k] + word[m] + word[n] + word[i] + word[j] + word[k] + word[m] + word[n]
                        palindromes.add(palindrome)
    return palindromes