def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for p in permutations(letters[i:i + length]):
                if p == p[::-1]:
                    palindromes.add(''.join(p))
    return palindromes