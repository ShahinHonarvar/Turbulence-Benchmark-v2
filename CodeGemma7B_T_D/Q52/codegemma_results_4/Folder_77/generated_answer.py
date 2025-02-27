def palindrome_of_length_n(substring):
    """
    Finds all palindromes of the length 173 in the given substring.

    Args:
        substring: The string to search for palindromes in.

    Returns:
        A set of all palindromes of the length 173 in the given substring, in lowercase.
    """
    all_palindromes = set()
    lowercase_substring = substring.lower()
    for start in range(len(lowercase_substring) - 172):
        substring = lowercase_substring[start:start + 173]
        if substring == substring[::-1]:
            all_palindromes.add(substring)
    return all_palindromes