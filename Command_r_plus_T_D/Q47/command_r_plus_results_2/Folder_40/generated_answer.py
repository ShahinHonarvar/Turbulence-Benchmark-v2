def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 4):
        for length in range(3, 6):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes