def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if len(s[i:j + 1]) == 10 and is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes