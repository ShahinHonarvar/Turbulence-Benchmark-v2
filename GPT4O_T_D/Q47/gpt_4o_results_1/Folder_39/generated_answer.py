def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[31:92]
    sanitized_s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for length in range(50, 54):
        for i in range(len(sanitized_s) - length + 1):
            substring = sanitized_s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes