def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 20):
        sub = s[i:i + 21]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes