def palindrome_of_length_n(s):

    def is_palindrome(x):
        return x == x[::-1] and x.isalpha()
    n = 84
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n].lower()
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes