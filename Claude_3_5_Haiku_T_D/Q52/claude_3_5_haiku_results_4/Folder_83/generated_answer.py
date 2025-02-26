def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 23):
        substring = s[start:start + 24]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return {p for p in palindromes if all((c.isalpha() for c in p))}