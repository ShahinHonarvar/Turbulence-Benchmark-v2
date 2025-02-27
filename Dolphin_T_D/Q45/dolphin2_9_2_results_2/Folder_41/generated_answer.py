import itertools

def palindromes_between_indices(string):
    subset_chars = [char for char in string[2:4]]
    palindromes = set()
    for p in range(3, len(subset_chars) + 1):
        for perm in itertools.permutations(subset_chars, p):
            for word in [''.join(perm), ''.join(reversed(perm))]:
                palindromes.add(word)
    return palindromes