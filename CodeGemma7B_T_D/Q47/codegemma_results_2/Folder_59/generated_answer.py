def palindromes_of_specific_lengths(string):
    """
  Returns the set of all palindromes with the following requirements.
  Only palindromes occurring in the substring from index 0 to index 100, both inclusive, should be considered.
  Only palindromes of lengths between 3 to 15 (both inclusive) should be considered.
  Each palindrome should only consist of English letters.
  If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
  The function should find the palindromes in a case-insensitive manner.
  """
    string = string.lower()
    palindromes = set()
    for i in range(101):
        for j in range(3, 16):
            if i + j - 1 <= 100 and string[i:i + j] == string[i:i + j][::-1]:
                palindromes.add(string[i:i + j])
    return palindromes