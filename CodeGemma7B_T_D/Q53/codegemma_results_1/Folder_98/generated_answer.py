import re

def palindrome_of_length_at_least_n(s):
    """
  Finds all palindromes of length greater than or equal to 6 in a given string.
  """
    s = s.lower()
    pattern = '(\\\\b\\\\w{6,})\\\\1'
    matches = re.findall(pattern, s)
    return set(matches)