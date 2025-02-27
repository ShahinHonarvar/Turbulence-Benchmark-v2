import itertools

def palindromes_between_indices(s):
    letters = [char for char in s[5:8] if char.isalpha()]
    lower_letters = [char.lower() for char in letters]
    palindromes = set()
    for length in range(3, len(lower_letters) + 1):
        for combination in itertools.permutations(lower_letters, length):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    return palindromes