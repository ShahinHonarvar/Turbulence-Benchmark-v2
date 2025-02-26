def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 76):
        substring = s[i:i + 77]
        if len(substring) == 77 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes