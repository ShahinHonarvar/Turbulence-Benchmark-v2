import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:6].lower() if c.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combination in itertools.combinations(letters, r):
            for p in itertools.permutations(combination):
                palindrome = ''.join(p)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes