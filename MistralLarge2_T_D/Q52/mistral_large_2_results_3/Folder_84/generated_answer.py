def palindrome_of_length_n(s):

    def is_palindrome(sub):
        sub = sub.lower()
        return sub == sub[::-1]
    n = 131
    palindromes = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub.isalpha() and is_palindrome(sub):
            palindromes.add(sub)
    return palindromes