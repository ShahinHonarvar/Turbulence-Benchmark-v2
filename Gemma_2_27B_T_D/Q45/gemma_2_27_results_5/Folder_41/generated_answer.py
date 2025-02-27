def palindromes_between_indices(text):
    substring = text[2:4]
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for i in range(len(letters), 2, -1):
        for perm in itertools.permutations(letters, i):
            candidate = ''.join(perm).lower()
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes