def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_letters_only(substr):
        return substr.isalpha()
    palindrome_set = set()
    for length in range(13, 43):
        for start in range(44, 100 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and is_letters_only(substring):
                palindrome_set.add(substring.lower())
    return palindrome_set