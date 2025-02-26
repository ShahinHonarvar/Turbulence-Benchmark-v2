from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[2:5] if c.isalpha()))

    def generate_palindromes(chars):
        palindrome_set = set()
        for length in range(4, len(chars) + 1):
            for perm in set(permutations(chars, length)):
                for arrangement in set(permutations(perm)):
                    candidate = ''.join(arrangement)
                    if candidate == candidate[::-1]:
                        palindrome_set.add(candidate)
        return palindrome_set
    return generate_palindromes(letters)