def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 39):
        substring = s[i:i + 40]
        if substring == substring[::-1]:
            palindromes.add(s[i:i + 40])
    return palindromes