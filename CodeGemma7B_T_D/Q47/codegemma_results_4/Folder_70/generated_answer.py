def palindromes_of_specific_lengths(s):
    """
  This function finds all palindromes of specific lengths in a string.
  The string must consist of any character.
  The function returns the set of all palindromes with the following requirements.
  Only palindromes occurring in the substring from index 10 to index 70, both inclusive, should be considered.
  Only palindromes of lengths between 24 to 52 (both inclusive) should be considered.
  Each palindrome should only consist of English letters.
  If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
  The function finds the palindromes in a case-insensitive manner.
  """
    substrings = []
    for i in range(10, 71):
        for j in range(i, 71):
            substring = s[i:j + 1]
            if len(substring) >= 24 and len(substring) <= 52:
                substrings.append(substring)
    palindromes = set()
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.add(substring)
    palindromes_list = list(palindromes)
    case_insensitive_palindromes = set()
    for palindrome in palindromes_list:
        case_insensitive_palindrome = palindrome.lower()
        case_insensitive_palindromes.add(case_insensitive_palindrome)
    return case_insensitive_palindromes