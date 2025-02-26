def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    if n < 173:
        return palindromes
    for i in range(n - 172):
        substring = s[i:i + 173]
        if len(substring) == 173 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes