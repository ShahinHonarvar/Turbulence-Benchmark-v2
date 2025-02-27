import re

def palindrome_of_length_at_least_n(s):
    """
  Finds all palindromes of the length greater than or equal to n that exist
  in the given string. Each palindrome should only consist of English letters.
  If no such palindromes exist in the given string, the function should
  return an empty set. The function should find the palindromes
  in a case-insensitive manner.

  Args:
    s: The string to search for palindromes.

  Returns:
    The set of all palindromes of the length greater than or equal to n
    that exist in the given string. If no such palindromes exist in the
    given string, the function should return an empty set.
  """
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = set()
    n = 112
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            s1 = s[i:j]
            if s1 == s1[::-1]:
                palindromes.add(s1)
    return palindromes