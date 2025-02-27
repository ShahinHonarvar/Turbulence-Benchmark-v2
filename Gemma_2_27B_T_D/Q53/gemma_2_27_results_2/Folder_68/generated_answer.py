def palindrome_of_length_at_least_n(s: str) -> set:
    palindromes = set()
    for i in range(len(s) - 20):
        for j in range(i + 20, len(s) + 1):
            substring = s[i:j]
            if substring.lower() == substring.lower()[::-1] and len(substring) >= 21:
                palindromes.add(substring)
    return palindromes