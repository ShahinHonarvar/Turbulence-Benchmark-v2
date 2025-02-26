from itertools import permutations

def palindromes_between_indices(s):
    letters = s[5:8]
    filtered_letters = ''.join((char.lower() for char in letters if char.isalpha()))

    def generate_palindromes(letters):
        palindromes = set()
        for length in range(3, len(letters) + 1):
            for perm in permutations(letters, length):
                for arrangement in set(permutations(perm)):
                    candidate = ''.join(arrangement)
                    if candidate == candidate[::-1] and len(candidate) >= 3:
                        palindromes.add(candidate)
        return palindromes
    return generate_palindromes(filtered_letters)