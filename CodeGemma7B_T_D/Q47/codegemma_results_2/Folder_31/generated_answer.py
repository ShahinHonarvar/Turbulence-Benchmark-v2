def palindromes_of_specific_lengths(text):
    """
          Takes one argument, a string. The given string may consist of any character.
          The function should return the set of all palindromes with the following requirements.
          Only palindromes occurring in the substring from index 11 to index 83, both inclusive, should be considered.
          Only palindromes of lengths between 37 to 60 (both inclusive) should be considered.
          Each palindrome should only consist of English letters.
          If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
          The function should find the palindromes in a case-insensitive manner.
          """
    substring = text[11:84]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 36, min(len(substring), i + 61)):
            if substring[i:j] == substring[j - 1:i - 1:-1]:
                palindrome = substring[i:j].lower()
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes