def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(5, 8) if s[i].isalpha()))
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for p in generate_palindromes(letters, length):
            palindromes.add(p)
    return palindromes

def generate_palindromes(letters, length):
    if length == 1:
        yield from letters
    else:
        for l in letters:
            for r in generate_palindromes(letters - {l}, length - 2):
                yield (l + r + l)