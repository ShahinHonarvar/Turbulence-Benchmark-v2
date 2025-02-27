from itertools import permutations

def palindromes_between_indices(s):
    s = s[:5].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 4):
        for c in letters:
            palindrome = ''.join(perm[:2] + [c] + list(reversed(perm[:2])))
            if palindrome not in palindromes:
                palindromes.add(palindrome)
    for perm in permutations(letters, 5):
        palindrome = ''.join(list(perm[:3]) + [perm[3]] + list(reversed(perm[:3])))
        if palindrome not in palindromes:
            palindromes.add(palindrome)
    return palindromes