def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def is_only_letters(substring):
        return substring.isalpha()
    palindrome_set = set()
    substring = s[32:72]
    for length in range(21, 33):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length].lower()
            if is_palindrome(candidate) and is_only_letters(candidate):
                palindrome_set.add(candidate)
    return palindrome_set