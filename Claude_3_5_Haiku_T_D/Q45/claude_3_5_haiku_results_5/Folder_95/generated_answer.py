from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    letters = [c.lower() for c in s[7:9] if c.isalpha()]
    if len(letters) < 3:
        return set()

    def generate_palindromes(chars):
        palindromes = set()
        for perm in set(permutations(chars)):
            for length in range(3, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    segment = perm[start:start + length]
                    if segment == segment[::-1]:
                        palindromes.add(''.join(segment))
        return palindromes
    return generate_palindromes(letters)