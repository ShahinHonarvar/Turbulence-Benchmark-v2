from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substr = s[:7]
    letters = [char for char in substr if char.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        result = set()
        for length in range(6, len(letters) + 1):
            for perm in permutations(letters, length):
                for arrangement in set(permutations(perm)):
                    candidate = ''.join(arrangement)
                    if is_palindrome(candidate):
                        result.add(candidate)
        return result
    return generate_palindromes(letters)