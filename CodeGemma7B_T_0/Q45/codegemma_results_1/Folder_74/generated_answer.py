from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(text):
    set_of_palindromes = set()
    for i in range(1, 6):
        for j in range(i + 1, 6 + 1):
            for p in permutations(text[i:j + 1].lower()):
                set_of_palindromes.add(''.join(p))
    if not set_of_palindromes:
        return set()
    return set_of_palindromes