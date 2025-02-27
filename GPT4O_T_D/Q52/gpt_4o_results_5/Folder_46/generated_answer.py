def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - 463):
        candidate = s[i:i + 464]
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes