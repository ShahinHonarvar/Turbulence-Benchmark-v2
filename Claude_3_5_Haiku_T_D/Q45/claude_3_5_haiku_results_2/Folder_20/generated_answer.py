from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters_count):
        unique_palindromes = set()
        for perm in set(permutations(letters_count)):
            for i in range(len(perm)):
                for j in range(i + 1, len(perm) + 1):
                    candidate = ''.join(perm[i:j] + perm[i:j - 1][::-1])
                    if len(candidate) >= 4 and is_palindrome(candidate):
                        unique_palindromes.add(candidate)
        return unique_palindromes
    return generate_palindromes(letters)