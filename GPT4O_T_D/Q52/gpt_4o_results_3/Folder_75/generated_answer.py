def palindrome_of_length_n(s):
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    for i in range(n - 79):
        substring = s[i:i + 80]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes