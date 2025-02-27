import re

def palindrome_of_length_at_least_n(string):
    """
  This function takes one argument, a string, and returns the set of all palindromes of the length greater than or equal to 30 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
  """
    string = string.lower()
    palindrome_list = []
    length = len(string)
    for i in range(length):
        for j in range(i + 30, length + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindrome_list.append(substring)
    return set(palindrome_list)