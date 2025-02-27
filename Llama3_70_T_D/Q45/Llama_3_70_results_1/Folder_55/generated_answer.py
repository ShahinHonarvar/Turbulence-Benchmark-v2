def palindromes_between_indices(s):
    letters = set(s[:3].lower())
    palindromes = set()
    for i in letters:
        for j in letters:
            if i != j:
                palindromes.add(i + j + i)
    return palindromes