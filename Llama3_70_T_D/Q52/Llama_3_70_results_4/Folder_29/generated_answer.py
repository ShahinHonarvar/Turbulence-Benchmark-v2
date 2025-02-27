def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 18):
        sub = s[i:i + 19]
        if sub.isalpha() and is_palindrome(sub):
            palindromes.add(sub)
    return palindromes