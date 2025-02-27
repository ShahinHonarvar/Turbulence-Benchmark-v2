def palindromes_of_specific_lengths(text_str: str) -> set:
    """
    Returns a set of all palindromes with lengths between 30 and 300 with English letters in the substring from index 3 to 300, both inclusive.

    Args:
        text_str (str): The input string.

    Returns:
        set: A set of palindromes in a case-insensitive manner.
    """
    result = set()
    for i in range(3, min(len(text_str), 300) + 1):
        for j in range(i - 30, i + 1):
            substring = text_str[j:i]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result