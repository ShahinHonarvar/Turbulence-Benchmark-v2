def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = ''.join([c.lower() for c in s[1:10] if c.isalpha()])
    for length in range(3, 8):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes