from collections import defaultdict

def palindrome_of_length_n(text):
    """
    Finds all palindromes of the length equal to 96 in a given string.

    Args:
      text: The string to search for palindromes.

    Returns:
      A set of all palindromes of the length equal to 96, or an empty set if there are no palindromes.
    """
    palindromes = set()
    text = text.lower()
    for i in range(len(text) - 95):
        for j in range(i + 1, len(text) - 95 + i):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes