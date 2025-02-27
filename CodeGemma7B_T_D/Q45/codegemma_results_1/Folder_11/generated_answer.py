from itertools import permutations

def palindromes_between_indices(string):
    """
  Returns the set of all palindromes of the length of at least 4 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 3 to index 7, both inclusive. If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set. The function should form each palindrome in a case-insensitive manner.
  """
    palindromes = set()
    for i in range(3, 8):
        for j in range(i, 8):
            substring = string[i:j + 1]
            for perm in permutations(substring.lower()):
                palindrome = ''.join(perm)
                if len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes