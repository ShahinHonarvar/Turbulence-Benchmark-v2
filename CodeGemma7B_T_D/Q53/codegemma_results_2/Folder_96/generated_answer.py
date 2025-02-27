def palindrome_of_length_at_least_n(s: str) -> set[str]:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 23):
        substring = s[i:i + 24]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes