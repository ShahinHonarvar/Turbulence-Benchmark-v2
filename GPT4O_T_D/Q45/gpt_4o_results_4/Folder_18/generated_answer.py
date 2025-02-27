from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:7]
    letters = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()

    def is_palindrome(seq):
        return seq == seq[::-1]
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            joined_perm = ''.join(perm)
            if is_palindrome(joined_perm):
                palindromes.add(joined_perm)
    return palindromes