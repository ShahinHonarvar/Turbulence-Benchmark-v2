def palindrome_of_length_n(s):
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    for i in range(n - 42):
        sub = s[i:i + 43]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes