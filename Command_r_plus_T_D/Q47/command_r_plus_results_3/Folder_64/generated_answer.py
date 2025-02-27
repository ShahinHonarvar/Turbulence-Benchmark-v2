def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 6):
        for j in range(i + 4, i + 7):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes