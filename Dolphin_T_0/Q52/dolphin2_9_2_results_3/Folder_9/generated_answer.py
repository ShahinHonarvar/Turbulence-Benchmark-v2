def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            sub = s[i:j]
            if len(sub) == 72 and is_palindrome(sub.lower()):
                palindromes.add(sub)
    return palindromes