def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(32, 74):
        for length in range(35, 42):
            if i + length > 79:
                break
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes