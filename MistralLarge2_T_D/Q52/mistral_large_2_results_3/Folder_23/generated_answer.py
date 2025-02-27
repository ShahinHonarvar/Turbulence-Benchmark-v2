def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    n = 69
    palindromes = set()
    for i in range(len(string) - n + 1):
        substr = string[i:i + n]
        if is_palindrome(substr) and substr.isalpha():
            palindromes.add(substr)
    return palindromes