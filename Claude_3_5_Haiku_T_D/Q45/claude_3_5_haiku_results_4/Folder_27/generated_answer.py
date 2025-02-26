from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindrome_set = set()
        unique_perms = set((''.join(p) for p in permutations(letters)))
        for perm in unique_perms:
            for length in range(6, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    substring = perm[start:start + length]
                    if is_palindrome(substring.lower()):
                        palindrome_set.add(substring.lower())
        return palindrome_set
    letters = [char for char in s[2:9] if char.isalpha()]
    if len(letters) < 6:
        return set()
    return generate_palindromes(letters)