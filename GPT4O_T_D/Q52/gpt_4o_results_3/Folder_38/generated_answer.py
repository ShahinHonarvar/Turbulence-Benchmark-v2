def palindrome_of_length_n(s):
    s = ''.join((c for c in s if c.isalpha())).lower()
    n = 38
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes