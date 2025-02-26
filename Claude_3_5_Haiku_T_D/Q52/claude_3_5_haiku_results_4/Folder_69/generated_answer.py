def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def contains_only_letters(substr):
        return substr.isalpha()
    n = 472
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if is_palindrome(substr) and contains_only_letters(substr):
            palindromes.add(substr)
    return palindromes