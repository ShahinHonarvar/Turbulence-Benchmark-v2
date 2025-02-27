def palindromes_of_specific_lengths(text):
    """
  This function finds the set of all palindromes of lengths 18 to 19 (inclusive) in the substring from index 27 to index 77 (inclusive) of a given string.
  The function converts the string to lowercase and only considers palindromes consisting of English letters.
  If no palindrome meets the requirements, the function returns an empty set.
  """
    text = text.lower()
    palindromes = set()
    for i in range(27, 78):
        for j in range(i + 18, i + 20):
            substring = text[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes