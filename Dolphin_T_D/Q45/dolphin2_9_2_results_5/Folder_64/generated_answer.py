from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:10] if c.isalpha()].lower()
    le = len(letters)
    palindrome_set = set()
    for i in range(5, le + 1):
        for p in permutations(letters, i):
            p = ''.join(p)
            if p == p[::-1]:
                palindrome_set.add(p)
    return palindrome_set