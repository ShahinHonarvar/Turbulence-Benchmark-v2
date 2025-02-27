def palindrome_of_length_n(s: str) -> set[str]:
    palindromes = set()
    for i in range(len(s) - 15):
        substring = s[i:i + 16]
        if substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes