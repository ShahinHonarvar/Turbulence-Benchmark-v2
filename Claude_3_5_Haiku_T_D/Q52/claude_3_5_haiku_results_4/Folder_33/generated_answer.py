def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    if n < 475:
        return palindromes
    for start in range(n - 474):
        substring = s[start:start + 475]
        if len(substring) == 475 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes