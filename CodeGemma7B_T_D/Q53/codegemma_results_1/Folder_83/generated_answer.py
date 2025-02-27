def palindrome_of_length_at_least_n(s):
    """
    Input: string
    Output: set of palindromes
    """
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) >= 60:
                palindrome_set.add(substring.lower())
    return palindrome_set