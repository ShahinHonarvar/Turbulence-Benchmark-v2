def palindromes_between_indices(s):
    chars = set(s[4:7].lower())
    if len(chars) < 2:
        return set()
    palindromes = set()
    for a in chars:
        for b in chars:
            if a != b:
                palindromes.add(a + b + a)
    return palindromes