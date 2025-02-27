def palindrome_of_length_n(s):

    def is_palindrome(x):
        return x.lower() == x.lower()[::-1]
    n = 474
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes