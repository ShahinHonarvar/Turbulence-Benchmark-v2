def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    n = 19
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substr = s[i:i + n]
        if is_palindrome(substr) and substr.isalpha():
            palindromes.add(substr.lower())
    return palindromes