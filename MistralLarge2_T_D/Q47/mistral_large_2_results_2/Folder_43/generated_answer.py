def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    palindromes = set()
    for length in range(23, 39):
        for i in range(41, 90 - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes