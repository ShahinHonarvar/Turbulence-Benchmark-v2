def palindromes_between_indices(string):
    for i in range(5):
        unique_letters = set((char.lower() for char in string[i:5] if char.isalpha()))
        if len(unique_letters) >= 3:
            permutations = set((''.join(p) for p in itertools.permutations(unique_letters)))
            palindromes = {word for word in permutations if word == word[::-1]}
            result.update(palindromes)
    return result or set()