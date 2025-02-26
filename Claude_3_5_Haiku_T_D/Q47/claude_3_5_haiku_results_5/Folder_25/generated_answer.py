def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def is_letter_only(substring):
        return substring.isalpha()
    palindrome_set = set()
    s = s.lower()
    for length in range(30, 47):
        for start in range(26, 85 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and is_letter_only(substring):
                palindrome_set.add(substring)
    return palindrome_set