from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    letters = s[4:6].lower()
    letters = [char for char in letters if char.isalpha()]
    if len(letters) < 3:
        return set()

    def generate_palindromes(chars):
        unique_palindromes = set()
        for perm in permutations(chars):
            for i in range(len(perm)):
                for j in range(i + 2, len(perm) + 1):
                    subset = perm[i:j]
                    if len(subset) >= 3:
                        candidate = subset + subset[:-1][::-1]
                        unique_palindromes.add(''.join(candidate))
        return unique_palindromes
    return generate_palindromes(letters)