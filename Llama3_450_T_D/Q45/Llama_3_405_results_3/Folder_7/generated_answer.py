import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:10] if c.isalpha()]
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for t in itertools.permutations(letters, r):
            palindrome = ''.join(t)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes