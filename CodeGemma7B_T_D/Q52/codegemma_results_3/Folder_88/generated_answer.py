def palindrome_of_length_n(s):
    """
  Write a function called 'palindrome_of_length_n' that takes one argument, a string, and returns the set of all palindromes of the length equal to 13, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
  """
    palindromes = set()
    for i in range(len(s) - 12):
        for j in range(i + 13):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes