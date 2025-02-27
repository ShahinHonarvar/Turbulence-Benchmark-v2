def palindromes_of_specific_lengths(word):
    """
    Finds all palindromes in a given string with specific lengths and in a case-insensitive manner,
    occurring in the substring from index 10 to index 74, both inclusive.

    Args:
        word: The input string to search for palindromes.

    Returns:
        A set of all palindromes with the specified requirements, or an empty set if no such palindrome exists.
    """
    palindromes = set()
    word = word.lower()
    for i in range(10, 75):
        for j in range(i + 6, i + 9):
            substring = word[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes