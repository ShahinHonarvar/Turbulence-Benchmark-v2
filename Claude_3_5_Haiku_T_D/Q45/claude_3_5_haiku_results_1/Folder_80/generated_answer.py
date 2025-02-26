from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindromes = set()
        for length in range(7, len(letters) + 1):
            for perm in permutations(letters, length):
                for arrangement in set(permutations(perm)):
                    word = ''.join(arrangement)
                    if is_palindrome(word):
                        palindromes.add(word)
        return palindromes
    return generate_palindromes(letters)