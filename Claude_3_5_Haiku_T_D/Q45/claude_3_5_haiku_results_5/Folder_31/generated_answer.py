from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:9] if char.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        unique_palindromes = set()
        for length in range(6, len(letters) + 1):
            for perm in permutations(letters, length):
                for p in [perm, perm[::-1]]:
                    candidate = ''.join(p)
                    if is_palindrome(candidate):
                        unique_palindromes.add(candidate)
        return unique_palindromes
    return generate_palindromes(letters)