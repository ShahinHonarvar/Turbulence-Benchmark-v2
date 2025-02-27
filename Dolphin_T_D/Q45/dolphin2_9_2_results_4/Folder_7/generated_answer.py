from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(s):
    indices = range(1, 10)
    letters = [s[i] for i in indices]
    letters = [char.lower() for char in letters if char.isalpha()]
    if len(set(letters)) < 3:
        return set()
    perms = [''.join(perm) for perm in permutations(letters, len(letters))]
    palindromes = [word for word in perms if word == word[::-1]]
    return set(palindromes)