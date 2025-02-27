def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    n = 64
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n].lower()
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes