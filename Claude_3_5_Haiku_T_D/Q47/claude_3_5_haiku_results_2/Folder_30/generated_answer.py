def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def is_letters_only(substring):
        return substring.isalpha()
    palindromes = set()
    for start in range(14, 91 - 55 + 1):
        for length in range(55, 72):
            substring = s[start:start + length].lower()
            if len(substring) == length and is_palindrome(substring) and is_letters_only(substring):
                palindromes.add(substring)
    return palindromes