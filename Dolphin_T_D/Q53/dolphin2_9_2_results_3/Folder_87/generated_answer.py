def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(18, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes