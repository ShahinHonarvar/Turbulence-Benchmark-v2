import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[2:10])).lower()
    letters = sorted(set(s))
    palindromes = set()
    for r in range(2, len(s) // 2 + 1):
        for p in itertools.permutations(letters, r):
            palindrome = ''.join(p) + ''.join(p[::-1])
            if len(palindrome) >= 4 and all((palindrome.count(c) <= s.count(c) for c in letters)):
                palindromes.add(palindrome)
    return palindromes