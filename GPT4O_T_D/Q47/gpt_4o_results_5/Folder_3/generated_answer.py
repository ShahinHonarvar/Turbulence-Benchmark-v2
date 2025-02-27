def palindromes_of_specific_lengths(s):

    def is_palindrome(ss):
        return ss == ss[::-1]
    sanitized = ''.join((c for c in s[27:96] if c.isalpha())).lower()
    palindromes = set()
    for length in range(49, 52):
        for i in range(len(sanitized) - length + 1):
            substring = sanitized[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes