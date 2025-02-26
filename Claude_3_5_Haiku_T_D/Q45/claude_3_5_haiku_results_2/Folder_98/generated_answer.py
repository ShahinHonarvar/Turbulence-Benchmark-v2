from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:6] if c.isalpha()]
    if len(letters) < 4:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 3, len(perm) + 1):
                subset = perm[i:j]
                if len(subset) >= 4:
                    palindrome = ''.join(subset + subset[::-1])
                    unique_palindromes.add(palindrome)
    return unique_palindromes