def palindromes_between_indices(s):
    letters = []
    for i in range(2, 8):
        letter = s[i].lower()
        if letter.isalpha():
            letters.append(letter)
    if len(set(letters)) < 7:
        return set()
    palindromes = set()
    for p in range(7, len(letters) + 1):
        for subset in itertools.combinations(letters, p):
            if subset == subset[::-1]:
                palindromes.add(''.join(subset))
    return palindromes