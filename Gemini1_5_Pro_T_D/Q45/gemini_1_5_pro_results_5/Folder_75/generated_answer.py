def palindromes_between_indices(string):
    letters = set([string[i].lower() for i in range(2, 5) if string[i].isalpha()])
    size = len(letters)
    if size < 3:
        return set()
    permutations = []

    def generate(current):
        if len(current) == size:
            permutations.append(''.join(current))
            return
        for letter in letters:
            if letter not in current:
                generate(current + [letter])
    generate([])
    palindromes = set()
    for permutation in permutations:
        if len(permutation) >= 3 and permutation == permutation[::-1]:
            palindromes.add(permutation)
    return palindromes