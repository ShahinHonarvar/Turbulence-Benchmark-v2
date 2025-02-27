def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 30, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes