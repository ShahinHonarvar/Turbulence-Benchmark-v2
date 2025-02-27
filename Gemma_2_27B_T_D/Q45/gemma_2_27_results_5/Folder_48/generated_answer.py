def palindromes_between_indices(s):
    letters = s[6:9].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for permutation in [''.join(p) for p in permutations([letters[i], letters[j], letters[k]])]:
                    if permutation == permutation[::-1] and len(permutation) >= 4:
                        palindromes.add(permutation)
    return palindromes