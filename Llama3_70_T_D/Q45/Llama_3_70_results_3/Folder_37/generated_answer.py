import itertools

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[1:5] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes