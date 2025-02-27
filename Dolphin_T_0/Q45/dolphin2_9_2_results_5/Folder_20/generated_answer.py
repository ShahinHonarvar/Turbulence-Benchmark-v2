from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:9] if char.isalpha()]
    palindrome_set = set()
    for i in range(4, len(letters) + 1):
        for perm in permutations(letters, i):
            palindromes = set()
            for p in palindrome_set:
                if p.islower() == ''.join(perm).islower():
                    palindrome_set.add(p)
            palindrome_set.add(''.join(perm))
    return palindrome_set