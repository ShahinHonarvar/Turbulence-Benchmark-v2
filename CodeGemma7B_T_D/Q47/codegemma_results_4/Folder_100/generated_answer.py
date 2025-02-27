def palindromes_of_specific_lengths(text):
    """
    Args:
        text: A string.

    Returns:
        A set of all palindromes with the following requirements:
        Only palindromes occurring in the substring from index 29 to index 96, both inclusive, should be considered.
        Only palindromes of lengths between 12 to 18 (both inclusive) should be considered.
        Each palindrome should only consist of English letters.
        If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
        The function should find the palindromes in a case-insensitive manner.
    """
    text = text.lower()
    substring = text[29:97]
    palindromes = set()
    for i in range(len(substring) - 11):
        for j in range(i + 12, len(substring) + 1):
            substring_to_check = substring[i:j]
            if substring_to_check == substring_to_check[::-1] and substring_to_check.isalpha():
                palindromes.add(substring_to_check)
    if not palindromes:
        return set()
    return palindromes