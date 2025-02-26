def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_letters_only(substring):
        return substring.isalpha()
    palindromes = set()
    for length in range(13, 50):
        for start in range(17, 96 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and is_letters_only(substring):
                palindromes.add(substring.lower())
    return palindromes