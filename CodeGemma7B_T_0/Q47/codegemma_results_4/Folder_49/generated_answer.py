def palindromes_of_specific_lengths(text):
    """
  This function takes a string as an argument and returns a set of all palindromes with the following requirements:
  Only palindromes occurring in the substring from index 10 to index 100, both inclusive, should be considered.
  Only palindromes of lengths between 10 to 50 (both inclusive) should be considered.
  Each palindrome should only consist of English letters.
  If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
  The function should find the palindromes in a case-insensitive manner.
  """
    palindromes = set()
    for i in range(10, 101):
        for j in range(i):
            substring = text[j:i]
            if substring == substring[::-1] and substring.isalpha() and (len(substring) in range(10, 51)):
                palindromes.add(substring.lower())
    return palindromes