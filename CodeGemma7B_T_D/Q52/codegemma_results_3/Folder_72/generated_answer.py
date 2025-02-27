from typing import Set

def palindrome_of_length_n(word: str) -> Set[str]:
    """
  Finds all palindromes of the length equal to 16, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
  """
    palindromes = set()
    word = word.lower()
    for i in range(len(word)):
        for j in range(i + 1, len(word)):
            substring = word[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes