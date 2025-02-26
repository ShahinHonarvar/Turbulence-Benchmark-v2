def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_letters_only(substring):
        return substring.isalpha()
    palindrome_set = set()
    for length in range(17, 56):
        for start in range(23, 95 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and is_letters_only(substring):
                palindrome_set.add(substring)
    return palindrome_set