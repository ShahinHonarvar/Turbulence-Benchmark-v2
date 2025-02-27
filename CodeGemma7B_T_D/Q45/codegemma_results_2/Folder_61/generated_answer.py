from itertools import permutations

def palindromes_between_indices(letters):
    result = set()
    letters = letters.lower()
    for start_idx in range(7):
        for end_idx in range(start_idx + 7, len(letters)):
            substring = letters[start_idx:end_idx + 1]
            permutations_list = permutations(substring)
            for permutation in permutations_list:
                if ''.join(permutation) in result:
                    continue
                result.add(''.join(permutation))
    return result