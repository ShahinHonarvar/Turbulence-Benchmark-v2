def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_only_letters(substring):
        return substring.isalpha()
    palindromes = set()
    for length in range(136, 161):
        for start in range(100, 296 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and is_only_letters(substring):
                palindromes.add(substring)
    return palindromes