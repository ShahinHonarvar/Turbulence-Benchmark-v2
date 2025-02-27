def palindromes_between_indices(s):
    sub = s[4:8]
    letters = [c.lower() for c in sub if c.isalpha()]
    palindromes = set()
    for c in letters:
        for i in range(4):
            for j in range(i + 2, 9):
                substring = sub[i:j]
                if substring == substring[::-1] and len(substring) >= 5:
                    palindromes.add(substring)
    return palindromes