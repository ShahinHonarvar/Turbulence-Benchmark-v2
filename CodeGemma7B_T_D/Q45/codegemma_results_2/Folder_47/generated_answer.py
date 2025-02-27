from itertools import permutations, choices

def palindromes_between_indices(string):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    combinations = permutations(alphabets)
    palindromes = set()
    for combination in combinations:
        for i in range(len(combination)):
            for j in range(i + 1, min(i + 5, len(combination) + 1)):
                if combination[i:j] in string[3:8].lower():
                    palindromes.add(''.join(combination).lower())
    return palindromes