def palindromes_between_indices(s):
    letters = s[6:10]
    palindromes = set()
    for i in range(0, len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    arrangement = letters[i] + letters[j] + letters[k] + letters[l]
                    if arrangement.lower() == arrangement.lower()[::-1]:
                        palindromes.add(arrangement)
    return palindromes