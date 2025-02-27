from collections import defaultdict

def palindromes_between_indices(s):
    substrings = [s[i:j] for i in range(6, 9) for j in range(i + 1, 9 + 1)]
    substrings = [substring for substring in substrings if any((letter.isalpha() for letter in substring))]
    palindromes = set()
    for substring in substrings:
        letters = sorted(list(set(filter(str.isalpha, substring))))
        permutations = generate_permutations(letters)
        for permutation in permutations:
            if permutation == permutation[::-1]:
                if len(permutation) >= 4:
                    palindromes.add(permutation)
    return palindromes

def generate_permutations(letters):
    if len(letters) == 0:
        return ['']
    permutations = []
    for i in range(len(letters)):
        first_letter = letters[i]
        remainder = letters[:i] + letters[i + 1:]
        for j in range(len(remainder)):
            remainder_j = remainder[:j] + remainder[j + 1:]
            for permutation in generate_permutations(remainder_j):
                permutations.append(first_letter + permutation)
    return permutations