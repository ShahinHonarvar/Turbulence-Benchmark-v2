from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):
        palindromes = set()
        unique_perms = set((''.join(p).lower() for p in permutations(chars) if len(p) >= 3))
        for perm in unique_perms:
            for i in range(len(perm) - 2):
                for j in range(i + 2, len(perm) + 1):
                    substr = perm[i:j]
                    if len(substr) >= 3 and is_palindrome(substr):
                        palindromes.add(substr)
        return palindromes
    letters_in_range = [c.lower() for c in s[2:7] if c.isalpha()]
    return generate_palindromes(letters_in_range)