import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.isalpha()]
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes