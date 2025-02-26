from itertools import permutations

def palindromes_between_indices(s):
    letters = s[3:6].lower()
    letters_only = ''.join((char for char in letters if char.isalpha()))

    def generate_palindromes(letters):
        palindromes = set()
        for length in range(3, len(letters) + 1):
            for perm in set(permutations(letters, length)):
                for p in [''.join(perm), ''.join(reversed(perm))]:
                    if p == p[::-1] and len(p) >= 3:
                        palindromes.add(p)
        return palindromes
    return generate_palindromes(letters_only)