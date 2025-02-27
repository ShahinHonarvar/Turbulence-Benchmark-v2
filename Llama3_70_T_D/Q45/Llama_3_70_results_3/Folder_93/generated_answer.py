from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:8].lower()
    letters = [char for char in s if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for perm in permutations(letters, r):
            if perm == perm[::-1]:
                palindrome = ''.join(perm)
                if len(palindrome) >= 6:
                    palindromes.add(palindrome)
    return palindromes