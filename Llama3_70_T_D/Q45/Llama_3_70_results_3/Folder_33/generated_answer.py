def palindromes_between_indices(s):
    letters = set((c.lower() for c in s[7:10] if c.isalpha()))
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in generate_palindromes(letters, length):
            palindromes.add(p)
    return palindromes

def generate_palindromes(letters, length):
    if length % 2 == 0:
        for p1 in generate_strings(letters, length // 2):
            yield (p1 + p1[::-1])
    else:
        for p1 in generate_strings(letters, length // 2):
            for c in letters:
                yield (p1 + c + p1[::-1])

def generate_strings(letters, length):
    if length == 1:
        for c in letters:
            yield c
    else:
        for c in letters:
            for p in generate_strings(letters, length - 1):
                yield (c + p)