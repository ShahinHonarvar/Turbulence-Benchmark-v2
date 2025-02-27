def palindrome_of_length_n(s):
    n = 17
    s = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(s[i:i + n])
    return palindromes