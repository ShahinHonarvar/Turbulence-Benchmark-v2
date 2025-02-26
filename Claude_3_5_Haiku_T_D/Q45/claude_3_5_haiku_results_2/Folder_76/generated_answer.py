from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:5]
    letters = [char.lower() for char in substring if char.isalpha()]
    palindrome_set = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            palindrome_candidate = ''.join(perm[:i + 1] + perm[i::-1])
            if len(palindrome_candidate) >= 4:
                palindrome_set.add(palindrome_candidate)
    return palindrome_set