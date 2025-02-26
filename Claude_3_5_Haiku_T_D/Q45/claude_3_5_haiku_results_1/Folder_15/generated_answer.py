from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        unique_palindromes = set()
        for perm in set(permutations(letters)):
            for i in range(len(perm)):
                for j in range(i + 3, len(perm) + 1):
                    candidate = ''.join(perm[i:j])
                    if is_palindrome(candidate) and len(candidate) >= 3:
                        unique_palindromes.add(candidate.lower())
        return unique_palindromes
    letters_in_range = [char.lower() for char in s[1:3] if char.isalpha()]
    return generate_palindromes(letters_in_range)