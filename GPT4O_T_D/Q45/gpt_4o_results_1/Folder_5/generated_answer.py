from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    letters = [char.lower() for char in s[4:9] if char.isalpha()]
    results = set()
    for r in range(4, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            word = ''.join(perm)
            if is_palindrome(word):
                results.add(word)
    return results