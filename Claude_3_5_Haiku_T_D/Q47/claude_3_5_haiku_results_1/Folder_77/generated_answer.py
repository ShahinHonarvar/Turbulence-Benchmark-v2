def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def is_letters_only(substring):
        return substring.isalpha()
    palindrome_set = set()
    for length in range(100, 170):
        for start in range(103, 277 - length + 1):
            substring = s[start:start + length].lower()
            if is_palindrome(substring) and is_letters_only(substring):
                palindrome_set.add(substring)
    return palindrome_set