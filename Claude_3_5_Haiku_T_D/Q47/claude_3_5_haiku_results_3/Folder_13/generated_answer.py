def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    results = set()
    for length in range(57, 61):
        for start in range(13, 96 - length + 1):
            substr = s[start:start + length].lower()
            if is_palindrome(substr) and is_only_letters(substr):
                results.add(substr)
    return results