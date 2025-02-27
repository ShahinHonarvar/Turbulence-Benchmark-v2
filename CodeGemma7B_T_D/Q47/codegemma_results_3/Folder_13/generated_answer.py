import re

def palindromes_of_specific_lengths(string):
    """
  Finds all palindromes with the following requirements:
    - Occurring in the substring from index 13 to index 95, both inclusive.
    - Of lengths between 57 to 60 (both inclusive).
    - Composed of English letters.
    - Case-insensitive.

  Args:
    string: The input string.

  Returns:
    A set of all palindromes satisfying the requirements.
  """
    pattern = re.compile('[A-Za-z]{57,60}')
    palindromes = set()
    for i in range(13, 96):
        for j in range(i + 57, i + 61):
            substring = string[i:j + 1]
            if pattern.fullmatch(substring):
                palindromes.add(substring)
    return palindromes