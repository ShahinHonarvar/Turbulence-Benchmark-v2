from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[5:10] if c.isalpha())).lower()
    if len(letters) < 6:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters, 6)):
        for i in range(3):
            half = perm[0:3]
            reverse_half = half[::-1]
            potential_palindrome = ''.join(half + perm[3:] + reverse_half)
            if potential_palindrome == potential_palindrome[::-1]:
                unique_palindromes.add(potential_palindrome)
    return unique_palindromes