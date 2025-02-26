from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    letters = [char.lower() for char in s[2:10] if char.isalpha()]
    if len(letters) < 4:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(4, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                subset = perm[start:start + length]
                if len(subset) >= 4:
                    palindrome = ''.join(subset + subset[::-1])
                    unique_palindromes.add(palindrome)
    return unique_palindromes