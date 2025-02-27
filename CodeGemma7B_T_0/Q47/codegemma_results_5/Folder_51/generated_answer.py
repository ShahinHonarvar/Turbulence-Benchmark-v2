def palindromes_of_specific_lengths(text):
    """
  This function takes one argument, a string.
  The given string may consist of any character.
  The function should return the set of all palindromes with the following requirements.
  Only palindromes occurring in the substring from index 2 to index 8, both inclusive, should be considered.
  Only palindromes of lengths between 3 to 4 (both inclusive) should be considered.
  Each palindrome should only consist of English letters.
  If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
  The function should find the palindromes in a case-insensitive manner.
  """
    palindromes = set()
    for i in range(2, 9):
        for j in range(i - 2, i + 1):
            substring = text[j:i + 1]
            if len(substring) in range(3, 5) and substring == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes