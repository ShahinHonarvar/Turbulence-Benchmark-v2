import itertools

def palindromes_between_indices(s):
    s = s[5:10].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combination in itertools.combinations(letters, r):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    return palindromes