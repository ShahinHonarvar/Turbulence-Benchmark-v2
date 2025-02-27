import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:10].lower() if c.isalpha()]
    if len(letters) < 7:
        return set()
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes