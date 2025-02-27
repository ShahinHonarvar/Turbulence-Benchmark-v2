def palindromes_between_indices(text):
    """
    Generates palindromes of length 5 or greater from a given string between indices 1 to 4 inclusive.

    Args:
        text: The string to generate palindromes from.

    Returns:
        A set of palindromes of length 5 or greater, or an empty set if no such palindromes exist.
    """
    substring = text[1:5]
    if not substring.lower().isalpha():
        return set()
    for arrangement in itertools.permutations(substring):
        palindrome = ''.join(arrangement)
        if palindrome == palindrome[::-1]:
            return {palindrome}
    return set()