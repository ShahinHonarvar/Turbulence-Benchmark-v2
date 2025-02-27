def palindrome_of_length_n(s):
    """
    Finds all palindromes of the length n in a string.

    Args:
      s: The string in which to find the palindromes.

    Returns:
      A set of all palindromes of the length n in the string, or an empty set if there are none.
    """
    ret = set()
    for i in range(len(s) - 34 + 1):
        j = i + 34
        if s[i:j].lower().replace(' ', '') == s[i:j].lower().replace(' ', '')[::-1]:
            ret.add(s[i:j])
    return ret