from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        unique_palindromes = set()
        for perm in set(permutations(letters)):
            candidate = ''.join(perm)
            for length in range(7, len(letters) + 1):
                for start in range(len(candidate) - length + 1):
                    subset = candidate[start:start + length]
                    if is_palindrome(subset):
                        unique_palindromes.add(subset)
        return unique_palindromes
    relevant_chars = [char.lower() for char in s[1:10] if char.isalpha()]
    return generate_palindromes(relevant_chars)