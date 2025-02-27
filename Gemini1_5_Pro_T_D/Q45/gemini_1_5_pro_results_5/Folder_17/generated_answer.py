def palindromes_between_indices(string: str) -> set:
    possible_letters = ''.join((char for i, char in enumerate(string) if 2 <= i <= 6 and char.isalpha()))
    return {''.join(permutation).lower() for i in range(4, len(possible_letters) + 1) for permutation in itertools.permutations(possible_letters, i) if ''.join(permutation).lower() == ''.join(reversed(''.join(permutation))).lower()}