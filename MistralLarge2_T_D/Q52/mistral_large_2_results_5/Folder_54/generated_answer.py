def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    n = 85
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes