def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 223
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if is_palindrome(substr):
            palindromes.add(substr)
    return palindromes