def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    start, end = (26, 90)
    palindromes = set()
    for length in range(27, 59):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes