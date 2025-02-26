def palindrome_of_length_at_least_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1] and substring.isalpha()
    palindromes = set()
    s = s.lower()
    for length in range(41, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes