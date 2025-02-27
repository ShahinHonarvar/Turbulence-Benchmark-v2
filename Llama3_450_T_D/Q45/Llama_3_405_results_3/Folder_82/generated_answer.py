import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for c in itertools.combinations(letters, r):
            for p in itertools.permutations(c):
                palindrome = ''.join(p)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes