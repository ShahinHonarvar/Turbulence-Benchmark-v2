import string

def palindrome_of_length_at_least_n(s):
    """
  Write a function called 'palindrome_of_length_at_least_n' that takes one argument, a string, and returns the set of all palindromes of the length greater than or equal to 13 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
  """
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 13, len(s) + 1):
            if s[i:j] == s[j - 1:i - 1:-1]:
                palindromes.add(s[i:j])
    return palindromes