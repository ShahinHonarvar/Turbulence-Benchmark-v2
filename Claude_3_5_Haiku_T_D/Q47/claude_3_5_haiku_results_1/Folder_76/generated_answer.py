def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def is_all_letters(substr):
        return substr.isalpha()
    result = set()
    for length in range(154, 183):
        for start in range(101, 293 - length + 1):
            substr = s[start:start + length].lower()
            if is_palindrome(substr) and is_all_letters(substr):
                result.add(substr)
    return result