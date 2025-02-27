def palindromes_between_indices(string):
    letters = [char.lower() for char in string[:6] if char.isalpha()]
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for j in combinations(letters, i):
            for p in permutations(j):
                word = ''.join(p)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes