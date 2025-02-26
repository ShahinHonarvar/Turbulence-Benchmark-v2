from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [char.lower() for char in s[3:7] if char.isalpha()]
    palindrome_set = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for candidate in [''.join(p) for p in [perm, perm[::-1]]]:
                if is_palindrome(candidate) and len(candidate) >= 3:
                    palindrome_set.add(candidate)
    return palindrome_set