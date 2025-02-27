def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    n = 25
    length = len(s)
    palindromes = set()
    for i in range(length - n + 1):
        sub = s[i:i + n]
        if is_palindrome(sub) and sub.isalpha():
            palindromes.add(sub)
    return palindromes