from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:4] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(chars):
        if len(chars) < 3:
            return set()
        result = set()
        for length in range(3, len(chars) + 1):
            for perm in permutations(chars, length):
                for arrangement in set(permutations(perm)):
                    if len(arrangement) >= 3:
                        candidate = ''.join(arrangement)
                        if candidate == candidate[::-1]:
                            result.add(candidate)
        return result
    return generate_palindromes(letters)