from typing import Set

def palindrome_of_length_n(text: str) -> Set[str]:
    """
    Write a function called 'palindrome_of_length_n' that takes one argument, a string, and returns the set of all palindromes of the length equal to 51, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    text = text.lower()
    length = 51
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + length):
            palindrome = text[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes