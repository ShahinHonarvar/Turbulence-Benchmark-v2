def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 83):
        substr = s[i:i + 84]
        if len(substr) == 84 and is_palindrome(substr) and substr.replace('', '').isalpha():
            palindromes.add(substr)
    return palindromes