from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    letters = s[4:6].lower()
    letters = [char for char in letters if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for r in range(3, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            for arrangement in set(permutations(perm)):
                possible_palindrome = list(arrangement)
                if possible_palindrome == possible_palindrome[::-1] and len(possible_palindrome) >= 3:
                    palindrome_set.add(''.join(possible_palindrome))
    return palindrome_set