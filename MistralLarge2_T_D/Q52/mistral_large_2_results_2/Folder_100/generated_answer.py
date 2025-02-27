def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = 91
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n].lower()
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes