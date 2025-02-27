def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    s = s[:31].lower()
    for length in range(20, 31):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes