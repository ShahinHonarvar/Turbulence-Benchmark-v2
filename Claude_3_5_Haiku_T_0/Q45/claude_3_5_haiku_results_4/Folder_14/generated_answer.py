from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    letters = s[4:6].lower()
    letter_set = set(letters)
    letter_set = {char for char in letter_set if char.isalpha()}
    if len(letter_set) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(letter_set) + 1):
        for perm in permutations(letter_set, length):
            for arrangement in set(permutations(perm)):
                candidate = list(arrangement)
                mirrored = candidate + candidate[-2::-1]
                palindrome = ''.join(mirrored)
                if len(palindrome) >= 3:
                    palindromes.add(palindrome)
    return palindromes