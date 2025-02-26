def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    if n < 97:
        return palindromes
    for start in range(n - 96):
        substring = s[start:start + 97]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes