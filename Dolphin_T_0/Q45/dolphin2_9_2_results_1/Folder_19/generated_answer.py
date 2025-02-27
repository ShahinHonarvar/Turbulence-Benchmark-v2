from itertools import permutations

def palindromes_between_indices(s):
    p = ''.join(s[1:8])
    p = p.lower()
    unique_letters = set(p) - {''}
    n = 7
    palindrome_set = set()
    for i in range(1, n + 1):
        for comb in permutations(unique_letters, i):
            palindrome = ''.join(comb)
            if palindrome == palindrome[::-1] and len(palindrome) >= n:
                palindrome_set.add(palindrome)
    return palindrome_set