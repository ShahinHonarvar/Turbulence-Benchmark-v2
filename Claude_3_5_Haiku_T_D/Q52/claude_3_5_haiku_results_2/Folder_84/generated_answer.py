def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_letters_only(substr):
        return substr.isalpha()
    palindromes = set()
    s_lower = s.lower()
    n = len(s)
    for start in range(n - 130):
        substr = s[start:start + 131]
        if len(substr) == 131 and is_letters_only(substr) and is_palindrome(substr):
            palindromes.add(substr)
    return palindromes