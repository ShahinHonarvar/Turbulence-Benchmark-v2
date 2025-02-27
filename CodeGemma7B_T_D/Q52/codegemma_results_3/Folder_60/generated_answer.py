from typing import Set

def palindrome_of_length_n(text: str) -> Set[str]:
    """
  This function takes one argument, a string, and returns the set of all palindromes of the length equal to 88, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
  """
    text = text.lower()
    text = ''.join((char for char in text if char.isalpha()))
    list_of_palindrome = []
    for i in range(len(text)):
        for j in range(i + 88, len(text) + 1):
            if text[i:j] == text[j - 1:i - 1:-1]:
                list_of_palindrome.append(text[i:j])
    return set(list_of_palindrome)