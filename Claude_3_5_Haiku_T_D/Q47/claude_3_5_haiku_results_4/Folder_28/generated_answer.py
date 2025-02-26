def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def contains_only_letters(substring):
        return substring.isalpha()
    substring = s[32:72].lower()
    palindromes = set()
    for length in range(21, 33):
        for start in range(len(substring) - length + 1):
            current = substring[start:start + length]
            if is_palindrome(current) and contains_only_letters(current):
                palindromes.add(current)
    return palindromes