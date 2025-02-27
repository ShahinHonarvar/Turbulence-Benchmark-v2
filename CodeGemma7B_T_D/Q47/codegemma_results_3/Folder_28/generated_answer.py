def palindromes_of_specific_lengths(text):
    """Returns the set of all palindromes with the specific requirements.

    Args:
    text: The input string containing any character.

    Returns:
    A set of palindromes occurring in the substring from index 32 to index 71, both inclusive, with lengths between 21 to 32 (both inclusive), consisting only of English letters, in a case-insensitive manner. Empty set if no palindrome matches the requirements.
    """
    target_substring = text[32:72].lower()
    palindromes = set()
    for i in range(len(target_substring)):
        for j in range(i + 21, min(i + 33, len(target_substring))):
            substring = target_substring[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes