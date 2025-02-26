from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:9] if char.isalpha()]
    if len(letters) < 4:
        return set()
    unique_palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            candidate = list(perm)
            if len(candidate) == length:
                left = candidate[:length // 2]
                right = candidate[length // 2:] if length % 2 == 0 else candidate[length // 2 + 1:]
                right.reverse()
                if left == right:
                    unique_palindromes.add(''.join(candidate))
    return unique_palindromes