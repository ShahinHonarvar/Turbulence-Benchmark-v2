def palindrome_of_length_n(s):
    n = 88
    palindromes = set()
    s = s.lower()
    length = len(s)

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(length - n + 1):
        substr = s[i:i + n]
        if is_palindrome(substr) and substr.isalpha():
            palindromes.add(substr)
    return palindromes