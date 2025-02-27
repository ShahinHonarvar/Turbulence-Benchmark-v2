def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[:51]
    palindromes = set()
    for length in range(50, 101):
        for i in range(0, 51 - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes