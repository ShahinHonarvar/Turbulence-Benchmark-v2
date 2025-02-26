def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_letters_only(substr):
        return substr.isalpha()
    palindromes = set()
    length = 475
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if is_palindrome(substr) and is_letters_only(substr):
            palindromes.add(substr)
    return palindromes