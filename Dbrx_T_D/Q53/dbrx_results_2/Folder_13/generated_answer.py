def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def find_palindromes(s, min_length):
    palindromes = set()
    for i in range(len(s) - min_length + 1):
        for j in range(i + min_length - 1, len(s)):
            substring = s[i:j + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes

def palindrome_of_length_at_least_n(s):
    return find_palindromes(s, 52)