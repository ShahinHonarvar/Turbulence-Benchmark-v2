def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    length = 210
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s) - length + 1):
        sub = s_lower[i:i + length]
        if sub.isalpha() and is_palindrome(sub):
            palindromes.add(s[i:i + length])
    return palindromes