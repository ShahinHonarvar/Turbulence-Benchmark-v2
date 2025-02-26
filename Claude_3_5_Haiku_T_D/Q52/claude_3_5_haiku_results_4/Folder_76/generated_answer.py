def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 256):
        substring = s[i:i + 257]
        if len(substring) == 257 and is_palindrome(substring) and is_letters_only(substring):
            palindromes.add(substring)
    return palindromes

def is_palindrome(s):
    return s == s[::-1]

def is_letters_only(s):
    return s.isalpha()