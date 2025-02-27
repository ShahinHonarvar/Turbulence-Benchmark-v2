from itertools import permutations

def palindromes_between_indices(s):
    letters = s[1:9]
    palindrome_set = set()
    for i in range(7, len(letters) + 1):
        palindromes = [''.join(p) for p in permutations(letters, i) if p == p[::-1]]
        for p in palindromes:
            palindrome_set.add(p.lower())
    return palindrome_set