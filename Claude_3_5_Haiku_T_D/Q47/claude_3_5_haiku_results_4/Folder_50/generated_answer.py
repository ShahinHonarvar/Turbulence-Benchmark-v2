def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    palindrome_set = set()
    if len(s) < 93:
        return palindrome_set
    substring = s[36:93]
    for length in range(10, 36):
        for start in range(len(substring) - length + 1):
            substr = substring[start:start + length]
            if is_palindrome(substr) and is_only_letters(substr):
                palindrome_set.add(substr.lower())
    return palindrome_set