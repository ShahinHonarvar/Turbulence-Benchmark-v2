def palindromes_of_specific_lengths(text):
    """
  This function takes one argument, a string.
  The given string may consist of any character.
  The function should return the set of all palindromes with the following requirements.
  Only palindromes occurring in the substring from index 26 to index 90, both inclusive, should be considered.
  Only palindromes of lengths between 27 to 58 (both inclusive) should be considered.
  Each palindrome should only consist of English letters.
  If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
  The function should find the palindromes in a case-insensitive manner.
  """
    text = text.lower()
    palindromes = set()
    for i in range(26, 91):
        for j in range(i, 91):
            substring = text[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 27 and (len(substring) <= 58):
                palindromes.add(substring)
    return palindromes