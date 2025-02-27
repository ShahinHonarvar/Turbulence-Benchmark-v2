def palindromes_between_indices(s):
    s = s[1:5].lower()
    letters = [char for char in s if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for arrangement in itertools.permutations(letters, length):
            if arrangement == arrangement[::-1]:
                palindromes.add(''.join(arrangement))
    return palindromes