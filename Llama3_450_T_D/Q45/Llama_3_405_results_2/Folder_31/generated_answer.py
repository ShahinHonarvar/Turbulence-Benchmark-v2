from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for r in range(6, len(s) + 1):
        for perm in permutations(s, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes