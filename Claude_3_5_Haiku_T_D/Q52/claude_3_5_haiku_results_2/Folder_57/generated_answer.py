def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    if n < 92:
        return palindromes
    for i in range(n - 91):
        substring = s[i:i + 92]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return {p for p in palindromes if all((char.isalpha() for char in p))}