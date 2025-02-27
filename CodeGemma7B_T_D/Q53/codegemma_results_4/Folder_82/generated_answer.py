def palindrome_of_length_at_least_n(string):
    """
  The function finds all palindromes of the length greater than or equal to 72 that exist in the given string.
  The function is case-insensitive. If no palindromes were found, the function returns an empty set.
  Args: string: the string to find palindrome in.
  Returns: a set of palindromes.
  """
    lowercase_string = string.lower()
    palindromes = set()
    for i in range(len(lowercase_string)):
        for j in range(len(lowercase_string), i, -1):
            substring = lowercase_string[i:j]
            if substring == substring[::-1]:
                if len(substring) >= 72:
                    palindromes.add(substring)
    return palindromes