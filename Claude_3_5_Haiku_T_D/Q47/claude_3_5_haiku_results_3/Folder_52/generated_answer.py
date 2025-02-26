def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def is_letters_only(substr):
        return substr.isalpha()
    palindromes = set()
    for length in range(13, 43):
        for start in range(44, 100 - length + 1):
            substring = s[start:start + length].lower()
            if is_palindrome(substring) and is_letters_only(substring):
                palindromes.add(substring)
    return palindromes