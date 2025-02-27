from collections import defaultdict
    import re

def palindromes_between_indices(given_string):
    english_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    palindromes = set()
    index_6, index_8 = (6, 8)
    if not 0 <= index_6 <= index_8 < len(given_string):
        return palindromes
    string_part = given_string[index_6:index_8 + 1]
    letter_counts = defaultdict(int)
    for letter in string_part:
        if letter in english_letters:
            letter_counts[letter] += 1
    for letter, count in letter_counts.items():
        if count < 3:
            continue
        permutations = []
        for i in range(3, count + 1):
            permutations += [''.join(p) for p in itertools.permutations(letter * i, i) if p[0] != ' ']
        palindromes.update(permutations)
    return {p for p in palindromes if p == p[::-1]}