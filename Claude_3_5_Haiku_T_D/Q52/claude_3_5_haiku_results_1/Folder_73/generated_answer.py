def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 40):
        substring = s[start:start + 41]
        if len(substring) == 41 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes