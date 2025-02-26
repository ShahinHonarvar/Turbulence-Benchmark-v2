def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def is_only_letters(substring):
        return substring.isalpha()
    palindromes = set()
    if len(s) < 85:
        return palindromes
    substring = s[30:85]
    for length in range(12, 21):
        for start in range(len(substring) - length + 1):
            current = substring[start:start + length].lower()
            if is_palindrome(current) and is_only_letters(current):
                palindromes.add(current)
    return palindromes