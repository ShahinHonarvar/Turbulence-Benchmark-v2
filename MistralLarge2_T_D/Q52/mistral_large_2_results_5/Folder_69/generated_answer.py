def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    n = 472
    palindromes = set()
    length = len(string)
    for i in range(length - n + 1):
        substr = string[i:i + n]
        if is_palindrome(substr) and substr.isalpha():
            palindromes.add(substr)
    return palindromes