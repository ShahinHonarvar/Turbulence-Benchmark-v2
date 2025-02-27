def palindrome_of_length_n(s: str) -> set:
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 43 + 1):
        substring = s[i:i + 43]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes