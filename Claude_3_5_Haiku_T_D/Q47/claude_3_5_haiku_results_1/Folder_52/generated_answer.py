def palindromes_of_specific_lengths(s):

    def is_letter_palindrome(substring):
        return substring.isalpha() and substring == substring[::-1]
    if len(s) < 100:
        return set()
    substr = s[44:100].lower()
    palindromes = set()
    for length in range(13, 43):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if is_letter_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes