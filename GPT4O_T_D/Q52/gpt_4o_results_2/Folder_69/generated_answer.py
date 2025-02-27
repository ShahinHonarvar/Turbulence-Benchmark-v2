def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    palindromes = set()
    length = 472
    if length > n:
        return palindromes
    for i in range(n - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes