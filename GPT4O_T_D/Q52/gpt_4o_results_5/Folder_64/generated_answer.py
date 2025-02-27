def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    palindromes = set()
    for i in range(n - 8):
        substring = s[i:i + 9]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes