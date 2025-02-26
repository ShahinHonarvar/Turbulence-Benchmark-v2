from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:5] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for palindrome_perm in set(permutations(perm)):
                candidate = ''.join(palindrome_perm)
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes