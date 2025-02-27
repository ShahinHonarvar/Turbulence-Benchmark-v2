def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = 401
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    if len(s) < n:
        return palindromes
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes