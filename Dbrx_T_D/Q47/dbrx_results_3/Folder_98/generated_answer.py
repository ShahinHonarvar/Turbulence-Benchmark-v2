def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join((e for e in s if e.isalpha()))
    palindromes = set()
    for length in range(5, 81):
        for i in range(21 - length + 1):
            substring = s[i:i + length].lower()
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes