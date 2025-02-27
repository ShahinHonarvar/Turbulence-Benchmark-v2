def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[3:10] if c.isalpha()]
    palindromes = set()
    for l in range(7, len(letters) + 1):
        for p in generate_palindromes(letters, l):
            palindromes.add(''.join(p))
    return palindromes

def generate_palindromes(letters, length):
    if length % 2 == 0:
        half = length // 2
        for first_half in generate_permutations(letters, half):
            yield (first_half + first_half[::-1])
    else:
        half = length // 2
        for first_half in generate_permutations(letters, half):
            for mid in letters:
                yield (first_half + [mid] + first_half[::-1])

def generate_permutations(letters, length):
    if length == 0:
        yield []
    else:
        for i, letter in enumerate(letters):
            remaining = letters[:i] + letters[i + 1:]
            for p in generate_permutations(remaining, length - 1):
                yield ([letter] + p)