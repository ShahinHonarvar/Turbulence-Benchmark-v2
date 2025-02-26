def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    n = len(s)
    palindromes = set()
    for i in range(n - 45):
        substring = s[i:i + 46]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes