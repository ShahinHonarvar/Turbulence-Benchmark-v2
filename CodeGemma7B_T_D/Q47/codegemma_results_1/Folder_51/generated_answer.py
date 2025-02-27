def palindromes_of_specific_lengths(text):
    """
    Finds all palindromes of lengths between 3 and 4 (inclusive) in the substring from index 2 to index 8, both inclusive, of the given text.

    Args:
        text: The text to search for palindromes in.

    Returns:
        A set of all palindromes of lengths between 3 and 4 (inclusive) in the substring from index 2 to index 8, both inclusive, of the given text. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    """
    text = text.lower()
    palindromes = set()
    for i in range(2, 9):
        for j in range(i + 2, 8):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes