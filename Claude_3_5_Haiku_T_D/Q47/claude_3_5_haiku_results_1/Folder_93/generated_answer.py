def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def is_only_letters(substring):
        return substring.isalpha()
    palindromes = set()
    for length in range(13, 50):
        for start in range(17, 96 - length + 1):
            substring = s[start:start + length].lower()
            if is_palindrome(substring) and is_only_letters(substring):
                palindromes.add(substring)
    return palindromes