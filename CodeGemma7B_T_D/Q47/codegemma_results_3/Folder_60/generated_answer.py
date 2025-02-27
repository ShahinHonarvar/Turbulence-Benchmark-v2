def palindromes_of_specific_lengths(text):
    """
    Args:
      text: A string.

    Returns:
      A set containing the palindrome in the given substring at the given length.
    """
    text = text[23:82]
    palindromes = set()
    for i in range(len(text) - 2):
        for j in range(i + 3, len(text)):
            substring = text[i:j]
            if substring == substring[::-1]:
                if len(substring) in range(32, 35):
                    palindromes.add(substring.lower())
    return palindromes