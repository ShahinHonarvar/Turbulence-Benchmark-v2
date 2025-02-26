from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [char.lower() for char in s[2:7] if char.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for candidate in [''.join(p) for p in [perm, perm[::-1]]]:
                if is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes