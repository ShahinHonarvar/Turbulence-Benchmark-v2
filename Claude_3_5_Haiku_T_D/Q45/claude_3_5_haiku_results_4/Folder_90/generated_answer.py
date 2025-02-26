def palindromes_between_indices(string):
    letters = [char.lower() for char in string[:6] if char.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            for perm in itertools.permutations(combination):
                candidate = ''.join(perm)
                if candidate == candidate[::-1] and len(candidate) >= 4:
                    palindromes.add(candidate)
    return palindromes