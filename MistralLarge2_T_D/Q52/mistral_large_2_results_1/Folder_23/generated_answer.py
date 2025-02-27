def palindrome_of_length_n(s):

    def is_palindrome(x):
        return x.lower() == x.lower()[::-1]
    n = 69
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes