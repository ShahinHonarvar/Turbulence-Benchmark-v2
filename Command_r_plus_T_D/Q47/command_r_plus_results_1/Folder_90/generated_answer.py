def palindromes_of_specific_lengths(s: str) -> set:
    s = s[105:281].lower()
    palindromes = set()
    for length in range(136, 152):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes