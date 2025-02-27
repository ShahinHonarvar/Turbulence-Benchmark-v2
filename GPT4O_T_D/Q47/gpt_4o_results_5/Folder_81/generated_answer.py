def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        normalized = ''.join([c for c in substr if c.isalpha()]).lower()
        return normalized == normalized[::-1]
    s = s[12:123]
    palindromes = set()
    for length in range(12, 221):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes