def palindrome_of_length_n(text):
    """
  Write a function called 'palindrome_of_length_n' that takes one argument, a string, and returns the set of all palindromes of the length equal to 16, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
  """
    return {word[i:i + 16] for word in text.lower().split() for i in range(len(word) - 15)}