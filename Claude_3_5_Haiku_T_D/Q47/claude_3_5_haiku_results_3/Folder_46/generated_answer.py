def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def is_letters_only(substr):
        return substr.isalpha()
    palindrome_set = set()
    for length in range(29, 63):
        for start in range(11, 98 - length + 1):
            substr = s[start:start + length].lower()
            if is_palindrome(substr) and is_letters_only(substr):
                palindrome_set.add(substr)
    return palindrome_set