def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s) - 39):
        substr = s[i:i + 40]
        if len(substr) == 40 and all((c.isalpha() for c in substr)) and is_palindrome(substr):
            palindromes.add(substr)
    return palindromes