def palindromes_between_indices(s):
    letters = ''.join(sorted([c.lower() for c in s[2:4]]))
    lengths = len(letters)
    if lengths < 3:
        return set()
    palindromes = set()
    for length in range(3, lengths + 1):
        for start in range(0, lengths - length + 1):
            end = start + length
            substring = letters[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes