from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[5:10] if char.isalpha()]
    palindrome_set = set()
    for r in range(4, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            for arrangement in set(permutations(perm)):
                word = ''.join(arrangement)
                if len(word) >= 4 and word == word[::-1]:
                    palindrome_set.add(word)
    return palindrome_set