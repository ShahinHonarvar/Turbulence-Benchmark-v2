def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    n = 257
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and all((char.isalpha() for char in substring)):
            palindromes.add(substring)
    return palindromes