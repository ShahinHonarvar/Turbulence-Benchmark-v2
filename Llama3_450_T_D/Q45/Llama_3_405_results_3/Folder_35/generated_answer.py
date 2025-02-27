import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:5] if c.isalpha()]
    letters = [c.lower() for c in letters]
    letters_set = set(letters)
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in itertools.permutations(letters_set, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes