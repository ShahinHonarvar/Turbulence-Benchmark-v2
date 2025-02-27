def palindromes_between_indices(s):
    """
    Finds all palindromes of length >= 3 that consist of the English letters in s
    occurring between index 0 and 2, inclusive. Acts case-insensitive.

    Args:
    s: String to construct palindromes from.

    Returns:
    Set of unique palindromes. Empty if none exist.
    """
    eligible_letters = set(s)[0:3]
    result = set()
    for i in eligible_letters:
        for j in eligible_letters:
            for k in eligible_letters:
                if (i, j, k) in [(i, j, k) for i in eligible_letters for j in eligible_letters for k in eligible_letters]:
                    palindrome = ''.join(sorted([i, j, k]))
                    result.add(palindrome)
    return result