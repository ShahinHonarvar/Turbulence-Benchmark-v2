import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:4] if c.isalpha()]
    palindromes = set()
    for r in range(2, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                palindrome = ''.join(perm)
                if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes