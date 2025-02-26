from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:7] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):
        palindrome_set = set()
        for length in range(3, len(chars) + 1):
            for perm in set(permutations(chars, length)):
                for arrangement in set(permutations(perm)):
                    word = ''.join(arrangement)
                    if is_palindrome(word):
                        palindrome_set.add(word)
        return palindrome_set
    return generate_palindromes(letters)