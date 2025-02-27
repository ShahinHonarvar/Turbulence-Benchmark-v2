import re

def palindrome_of_length_at_least_n(text):
    """
  This function returns the set of all palindromes of the length greater than or equal to 119
  that exist in the given string. Each palindrome should only consist of English letters.
  If no such palindromes exist in the given string, the function should return an empty set.
  The function should find the palindromes in a case-insensitive manner.
  """
    pattern = re.compile('(?i)(\\\\b[a-z]{119,}\\\\b)')
    return set(pattern.findall(text))