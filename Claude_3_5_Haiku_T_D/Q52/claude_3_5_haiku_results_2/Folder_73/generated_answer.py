def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_letters_only(substr):
        return substr.isalpha()
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s) - 40):
        substr = s[i:i + 41]
        if len(substr) == 41 and is_palindrome(substr) and is_letters_only(substr):
            palindromes.add(substr)
    return palindromes