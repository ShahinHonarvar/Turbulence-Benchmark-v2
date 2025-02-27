import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[3:9] if c.isalpha()]
    letters = [c.lower() for c in letters]
    letters = list(set(letters))
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes