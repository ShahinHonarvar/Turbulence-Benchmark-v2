from itertools import permutations
  import re

def palindromes_between_indices(text):
    """
  This function takes a string as an argument and returns the set of all palindromes of the length of at least 7 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 1 to index 7, both inclusive. If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set. The function should form each palindrome in a case-insensitive manner.
  """
    text = re.sub('[^a-zA-Z]', '', text)
    if len(text) < 7:
        return set()
    palindromes = set()
    for i in range(len(text) - 6):
        for j in range(i + 7, len(text) + 1):
            for p in permutations(text[i:j]):
                palindromes.add(''.join(p))
    return palindromes