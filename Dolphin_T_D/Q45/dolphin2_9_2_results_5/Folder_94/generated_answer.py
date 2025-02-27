def palindromes_between_indices(string):
    substring = string[3:5]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            permutations = set(substring[i:j + 1])
            for p in permutations:
                if p.lower() == p.lower()[::-1] and len(p.lower()) >= 3:
                    palindromes.add(p)
    return palindromes