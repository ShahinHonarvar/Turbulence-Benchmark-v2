def palindromes_of_specific_lengths(text: str) -> set[str]:
    """
    Finds all palindromes of lengths between 18 to 36 in the substring from index 10 to 59 (inclusive) in the given text.

    Args:
        text: The input text to search for palindromes.

    Returns:
        A set of all palindromes that meet the specified requirements.
    """
    text = text.lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(10, 60):
        for j in range(i + 18, i + 37):
            substring = text[i:j]
            if substring == substring[::-1] and set(substring).issubset(valid_chars):
                palindromes.add(substring)
    return palindromes