from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:5].lower()))
    if len(s) < 4:
        return set()
    palindromes = set()
    for r in range(4, len(s) + 1):
        for p in permutations(s, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes