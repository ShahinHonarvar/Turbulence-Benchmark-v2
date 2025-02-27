def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    n = 56
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring.lower()):
            palindromes.add(substring.lower())
    return palindromes