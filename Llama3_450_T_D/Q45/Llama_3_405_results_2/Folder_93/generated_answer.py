from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:8].lower()
    counter = Counter((c for c in s if c.isalpha()))
    palindromes = set()
    for r in range(6, sum(counter.values()) + 1):
        for p in permutations(''.join((c * n for c, n in counter.items())), r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes