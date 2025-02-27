def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    s = s[125:284]
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    palindromes = set()
    for length in range(109, 127):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes