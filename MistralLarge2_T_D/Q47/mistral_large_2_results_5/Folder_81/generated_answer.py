def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = s[12:123].lower()
    palindromes = set()
    for length in range(12, 221):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if substr.isalpha() and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes