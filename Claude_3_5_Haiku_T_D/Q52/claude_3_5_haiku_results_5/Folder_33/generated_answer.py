def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    if 475 > n:
        return palindromes
    for i in range(n - 474):
        substring = s[i:i + 475]
        if len(substring) == 475 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes