def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for length in range(12, 221):
        for start in range(12, 123 - length + 1):
            substr = s[start:start + length]
            if substr.isalpha() and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes