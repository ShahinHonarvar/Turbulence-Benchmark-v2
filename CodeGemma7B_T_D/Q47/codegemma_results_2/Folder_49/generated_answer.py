def palindromes_of_specific_lengths(text: str) -> set:
    """
    Finds palindromes in a given string with specific length and range.

    Args:
    text: The input string.

    Returns:
    A set of palindromes that meet the given requirements.
    """
    alphanumeric_text = ''.join((char for char in text if char.isalnum()))
    a_to_z_text = ''.join((char for char in alphanumeric_text if char.isalpha()))
    palindromes = set()
    for i in range(9, len(a_to_z_text) - 9):
        for j in range(11, len(a_to_z_text) - i + 10):
            substring = a_to_z_text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes