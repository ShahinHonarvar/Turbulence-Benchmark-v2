from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(letters):
        palindromes = set()
        for length in range(3, len(letters) + 1):
            for perm in permutations(letters, length):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word.lower())
        return palindromes
    if len(s) < 5:
        return set()
    target_slice = s[1:5]
    letters = [c.lower() for c in target_slice if c.isalpha()]
    return generate_palindromes(letters)