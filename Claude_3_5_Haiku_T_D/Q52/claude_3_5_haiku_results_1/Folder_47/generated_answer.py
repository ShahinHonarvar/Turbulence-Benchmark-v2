def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 33):
        substring = s[start:start + 34]
        if len(substring) == 34 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes