from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:6] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            for palindrome_perm in set(permutations(perm)):
                candidate = ''.join(palindrome_perm)
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes