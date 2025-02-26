def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_english_letters(substring):
        return all((char.isalpha() for char in substring))
    palindrome_set = set()
    for length in range(3, 61):
        for start in range(70, 141 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and is_english_letters(substring):
                palindrome_set.add(substring.lower())
    return palindrome_set