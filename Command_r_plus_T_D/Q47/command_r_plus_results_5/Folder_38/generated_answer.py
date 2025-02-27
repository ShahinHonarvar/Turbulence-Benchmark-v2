def palindromes_of_specific_lengths(s: str) -> set:
    s = s[18:88]
    palindromes = set()
    for length in range(38, 61):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes