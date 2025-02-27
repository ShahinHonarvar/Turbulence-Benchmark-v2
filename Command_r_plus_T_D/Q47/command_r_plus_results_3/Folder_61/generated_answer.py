def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for length in range(20, 31):
        for start in range(len(s) - length + 1):
            if start <= 30:
                substring = s[start:start + length]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes