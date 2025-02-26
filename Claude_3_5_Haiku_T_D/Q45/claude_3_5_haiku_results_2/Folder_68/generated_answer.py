from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindrome_set = set()
        for length in range(4, len(letters) + 1):
            for perm in set(permutations(letters, length)):
                for arrangement in set(permutations(perm)):
                    word = ''.join(arrangement).lower()
                    if is_palindrome(word):
                        palindrome_set.add(word)
        return palindrome_set
    letters = [c.lower() for c in s[1:9] if c.isalpha()]
    return generate_palindromes(letters)