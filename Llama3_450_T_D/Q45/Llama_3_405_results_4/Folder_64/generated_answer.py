from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:10].lower() if c.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for p in permutations(letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes