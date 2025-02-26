from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]

    def create_palindromes(chars):
        palinds = set()
        for perm in set(permutations(chars)):
            for i in range(len(perm)):
                for j in range(i + 3, len(perm) + 1):
                    candidate = perm[i:j]
                    if len(candidate) >= 3 and candidate == candidate[::-1]:
                        palinds.add(''.join(candidate))
        return palinds
    return create_palindromes(letters)