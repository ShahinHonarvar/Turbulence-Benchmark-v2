def palindromes_between_indices(string):
    letters = []
    for i in range(3, 7):
        if string[i].isalpha():
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for permutation in [''.join(p) for p in permutations_with_repetition(letters[i:l + 1])]:
                        if len(permutation) >= 4 and permutation == permutation[::-1]:
                            palindromes.add(permutation)
    return palindromes

def permutations_with_repetition(letters):
    if len(letters) == 1:
        return [letters]
    permutations = []
    for i in range(len(letters)):
        remaining_letters = letters[:i] + letters[i + 1:]
        for permutation in permutations_with_repetition(remaining_letters):
            permutations.append([letters[i]] + permutation)
    return permutations