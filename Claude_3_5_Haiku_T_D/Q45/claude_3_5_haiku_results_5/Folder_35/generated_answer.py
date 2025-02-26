from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:5] if char.isalpha()]
    if len(letters) < 4:
        return set()

    def generate_palindromes(chars):
        unique_pals = set()
        for perm in set(permutations(chars)):
            for i in range(len(perm)):
                for j in range(i + 1, len(perm) + 1):
                    candidate = perm[i:] + perm[:i]
                    candidate_str = ''.join(candidate)
                    if len(candidate_str) >= 4 and candidate_str == candidate_str[::-1]:
                        unique_pals.add(candidate_str)
        return unique_pals
    return generate_palindromes(letters)