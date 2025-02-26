def palindrome_of_length_at_least_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    palindromes = set()
    s = s.lower()
    for length in range(46, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and substring.replace(' ', '').isalpha():
                palindromes.add(substring)
    return palindromes