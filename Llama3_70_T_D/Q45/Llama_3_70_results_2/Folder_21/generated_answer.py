from itertools import permutations

def generate_palindromes(chars):
    for perm in permutations(chars, 7):
        first_half = ''.join(perm[:4])
        second_half = first_half[::-1]
        yield (first_half + second_half + perm[4:])
    for perm in permutations(chars, 8):
        first_half = ''.join(perm[:4])
        second_half = first_half[::-1]
        yield (first_half + perm[4] + second_half)

def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(1, 9) if s[i].isalpha()))
    return set(generate_palindromes(letters))