from itertools import permutations

def palindromes_between_indices(s):
    section = s[:6].lower()
    letters = [c for c in section if c.isalpha()]
    letter_set = set(letters)
    palindromes = set()
    if len(letter_set) < 3:
        return palindromes
    letter_list = list(letters)
    for i in range(6, len(letter_list) + 1):
        for p in permutations(letter_list, i):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes