import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:5])).lower()
    letters = sorted(set(s))
    palindromes = set()
    for r in range(2, len(s) + 1):
        for p in itertools.product(letters, repeat=r):
            palindrome = ''.join(p) + ''.join(p[::-1])
            if len(palindrome) >= 4 and all((palindrome.count(c) <= s.count(c) for c in letters)):
                palindromes.add(palindrome)
    return palindromes