def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 185):
        substring = s[i:i + 186]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes