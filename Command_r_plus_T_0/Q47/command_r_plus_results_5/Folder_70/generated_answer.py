def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s[10:71].lower()
    palindromes = set()
    for length in range(24, 53):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes