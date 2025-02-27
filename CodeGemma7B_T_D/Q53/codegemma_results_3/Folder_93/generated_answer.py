def palindrome_of_length_at_least_n(s):
    """
    This function returns the set of all palindromes of the length greater than or equal to 90 that exist in the given string.
    Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    palindrome = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            w = s[i:j + 1].lower()
            if w == w[::-1] and len(w) >= 90:
                palindrome.add(w)
    return palindrome