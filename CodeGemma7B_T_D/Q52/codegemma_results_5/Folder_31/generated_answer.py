import re

def palindrome_of_length_n(s):
    """
  Returns the set of all palindromes of the length equal to 66,
  where each palindrome is a substring of the given string.
  Each palindrome should only consist of English letters.
  If there is no palindrome of the specified length as a substring
  of the given string, the function should return an empty set.
  The function should find the palindromes in a case-insensitive manner.
  """
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 65):
        substring = s[i:i + 66]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes