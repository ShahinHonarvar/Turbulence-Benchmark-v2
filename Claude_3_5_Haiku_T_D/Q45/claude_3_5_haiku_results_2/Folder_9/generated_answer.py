from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palinds = set()
        for perm in set(permutations(letters)):
            for length in range(7, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    candidate = ''.join(perm[start:start + length])
                    if is_palindrome(candidate):
                        palinds.add(candidate)
        return palinds
    letters = [char.lower() for char in s[0:7] if char.isalpha()]
    return generate_palindromes(letters)