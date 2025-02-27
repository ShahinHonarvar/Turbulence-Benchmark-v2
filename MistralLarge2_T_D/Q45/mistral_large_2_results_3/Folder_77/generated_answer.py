def palindromes_between_indices(s):
    substring = s[4:7].lower()
    letters = set(substring)
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                if a == c:
                    palindromes.add(a + b + c + b + a)
                    palindromes.add(a + b + b + a)
    return {p for p in palindromes if len(p) >= 4}