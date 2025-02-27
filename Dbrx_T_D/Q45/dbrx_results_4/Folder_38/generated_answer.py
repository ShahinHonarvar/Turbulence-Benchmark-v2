def palindromes_between_indices(s):
    letters = [c.lower() for c in s if c.isalpha()]
    if len(letters) < 5 or len(letters) - 4 < 5:
        return set()
    palindromes = set()
    for i in range(3, len(letters) - 4):
        for j in range(i, len(letters)):
            combination = letters[i:j + 1]
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    return palindromes