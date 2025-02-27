def palindrome_of_length_n(s):

    def is_palindrome(st):
        return st == st[::-1]
    n = 74
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if is_palindrome(substr):
            palindromes.add(substr)
    return palindromes