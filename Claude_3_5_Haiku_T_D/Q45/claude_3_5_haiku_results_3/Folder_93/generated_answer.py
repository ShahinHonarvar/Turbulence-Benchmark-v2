from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:8]
    letters = [char.lower() for char in substring if char.isalpha()]
    palindrome_set = set()
    if len(letters) < 6:
        return palindrome_set
    for perm in set(permutations(letters, 6)):
        for arrangement in [list(perm), list(reversed(perm))]:
            if arrangement == list(arrangement)[::-1]:
                palindrome = ''.join(arrangement)
                if len(palindrome) >= 6:
                    palindrome_set.add(palindrome)
    return palindrome_set