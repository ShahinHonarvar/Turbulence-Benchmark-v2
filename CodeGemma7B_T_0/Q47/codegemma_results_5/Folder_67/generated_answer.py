def palindromes_of_specific_lengths(text):
    """
    Finds all palindromes of specific lengths in a given string.

    Args:
        text: The string to search for palindromes in.

    Returns:
        A set of all palindromes of lengths between 26 to 33 (inclusive)
        occurring in the substring from index 65 to index 99 (inclusive),
        or an empty set if no such palindrome exists.
    """
    text = text.lower()
    palindromes = set()
    for i in range(65, 100):
        for j in range(i - 25, i + 1):
            if j < 0 or j > len(text) - 1:
                continue
            if text[i] == text[j]:
                palindrome = text[j:i + 1]
                if len(palindrome) >= 26 and len(palindrome) <= 33:
                    palindromes.add(palindrome)
    return palindromes