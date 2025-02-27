def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    n = 24
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if is_palindrome(substr) and substr.isalpha():
            palindromes.add(substr)
    return palindromes