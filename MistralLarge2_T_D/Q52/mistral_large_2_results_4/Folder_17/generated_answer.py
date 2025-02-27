def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    length = 289
    palindromes = set()
    n = len(s)
    for i in range(n - length + 1):
        substring = s[i:i + length]
        if is_palindrome(substring):
            palindromes.add(substring.lower())
    return palindromes