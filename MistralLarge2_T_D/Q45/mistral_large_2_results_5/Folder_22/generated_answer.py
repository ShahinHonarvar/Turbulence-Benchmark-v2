import itertools

def palindromes_between_indices(s):
    letters = [char for char in s[5:7] if char.isalpha()]
    lower_letters = [char.lower() for char in letters]
    palindromes = set()
    for length in range(3, len(lower_letters) + 1):
        for comb in itertools.combinations_with_replacement(lower_letters, length):
            if comb == comb[::-1]:
                palindromes.add(''.join(comb))
    return palindromes