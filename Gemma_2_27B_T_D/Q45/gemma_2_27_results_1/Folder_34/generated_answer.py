def palindromes_between_indices(s):
    letters = s[5:8].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for perm in permutations([letters[i], letters[j], letters[k]]):
                    pal = ''.join(perm) + ''.join(reversed(perm))
                    if len(pal) >= 4 and pal[::-1] == pal:
                        palindromes.add(pal)
    return palindromes