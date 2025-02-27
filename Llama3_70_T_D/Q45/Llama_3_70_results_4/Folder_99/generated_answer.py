from itertools import combinations_with_replacement, permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in combinations_with_replacement(letters, r):
            for perm in permutations(combo, r):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes