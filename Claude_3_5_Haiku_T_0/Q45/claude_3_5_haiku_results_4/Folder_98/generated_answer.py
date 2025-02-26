from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:6] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = list(perm)
            candidate.extend(reversed(candidate[:-1]))
            palindrome = ''.join(candidate)
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes