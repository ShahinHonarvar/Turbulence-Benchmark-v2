def palindrome_of_length_at_least_n(s):
    """
    Returns the set of all palindromes of the length greater than or equal to 44 that exist in the given string.
    """
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s[i:j + 1]):
                result.add(s[i:j + 1])
    return result

def is_palindrome(s):
    """
    Checks if the given string is a palindrome.
    """
    if len(s) < 44:
        return False
    return s == s[::-1]