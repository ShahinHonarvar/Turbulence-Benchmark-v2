def palindromes_between_indices(s: str) -> set:
    s = s[1:10].lower()
    letters = set(s)
    palindromes = set()
    for c in letters:
        for length in range(7, len(s) + 1):
            substring = s[0 - length:s.index(c)] + c + s[s.index(c) + 1:s.index(c)] + s[s.index(c):]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes