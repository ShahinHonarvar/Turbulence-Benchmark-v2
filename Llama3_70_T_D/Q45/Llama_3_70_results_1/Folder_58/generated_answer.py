from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 6):
        if perm == perm[::-1]:
            palindrome = ''.join(perm)
            if palindrome not in palindromes:
                palindromes.add(palindrome)
    return palindromes