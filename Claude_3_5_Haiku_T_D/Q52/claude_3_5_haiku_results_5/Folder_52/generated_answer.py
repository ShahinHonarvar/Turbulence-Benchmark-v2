def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    n = 423
    palindromes = set()
    if len(s) < n:
        return palindromes
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if is_palindrome(substr) and all((c.isalpha() for c in substr)):
            palindromes.add(substr)
    return palindromes