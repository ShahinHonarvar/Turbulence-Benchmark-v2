def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_only_letters(substring):
        return substring.isalpha()
    palindromes = set()
    for start in range(15, 87 - 50):
        for length in range(51, 61):
            substring = s[start:start + length]
            if len(substring) == length and is_palindrome(substring) and is_only_letters(substring):
                palindromes.add(substring)
    return palindromes