def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 96, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes