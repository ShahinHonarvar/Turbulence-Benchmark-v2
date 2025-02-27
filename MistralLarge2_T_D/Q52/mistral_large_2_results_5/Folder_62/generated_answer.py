def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    n = 188
    palindromes = set()
    length = len(s)
    if length < n:
        return palindromes
    for i in range(length - n + 1):
        substr = s[i:i + n]
        if is_palindrome(substr):
            palindromes.add(substr)
    return palindromes