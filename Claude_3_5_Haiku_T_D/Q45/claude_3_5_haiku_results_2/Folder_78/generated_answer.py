from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[6:9] if char.lower().isalpha()]
    if len(letters) < 3:
        return set()

    def generate_palindromes(chars):
        unique_palindromes = set()
        for perm in set(permutations(chars)):
            if len(perm) >= 3:
                half_len = len(perm) // 2
                first_half = perm[:half_len]
                last_half = perm[len(perm) - half_len:][::-1]
                if first_half == last_half:
                    unique_palindromes.add(''.join(perm))
        return unique_palindromes
    return generate_palindromes(letters)