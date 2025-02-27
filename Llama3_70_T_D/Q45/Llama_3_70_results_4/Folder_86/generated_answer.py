def palindromes_between_indices(s):
    letters = set((c for c in s[6:10].lower() if c.isalpha()))
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in generate_palindromes(letters, length):
            palindromes.add(p)
    return palindromes

def generate_palindromes(letters, length):
    if length % 2 == 0:
        for p1 in generate_combinations(letters, length // 2):
            yield (p1 + p1[::-1])
    else:
        for p1 in generate_combinations(letters, length // 2):
            for c in letters:
                yield (p1 + c + p1[::-1])

def generate_combinations(letters, length):
    if length == 0:
        yield ''
    else:
        for c in letters:
            for p in generate_combinations(letters - {c}, length - 1):
                yield (c + p)