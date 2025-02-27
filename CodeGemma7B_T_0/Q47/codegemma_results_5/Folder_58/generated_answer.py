import re

def palindromes_of_specific_lengths(text):
    """
  This function takes a string and returns the set of all palindromes
  with the following requirements:
  - Only palindromes occurring in the substring from index 125 to index 283, both inclusive, should be considered.
  - Only palindromes of lengths between 109 to 126 (both inclusive) should be considered.
  - Each palindrome should only consist of English letters.
  - If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
  - The function should find the palindromes in a case-insensitive manner.
  """
    text = text.lower()
    pattern = re.compile('(?<=.{125})([a-z]{109,126})(?=.{283})')
    return {word for word in re.findall(pattern, text)}