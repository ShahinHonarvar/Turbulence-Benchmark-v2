from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindrome_set = set()
        for length in range(6, len(letters) + 1):
            for perm in permutations(letters, length):
                for arrangement in set(permutations(perm)):
                    candidate = ''.join(arrangement)
                    if is_palindrome(candidate):
                        palindrome_set.add(candidate)
        return palindrome_set
    substring = s[:7].lower()
    letters = [char for char in substring if char.isalpha()]
    return generate_palindromes(letters)