def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = 95
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_palindrome(sub):
            palindromes.add(sub)
    return palindromes