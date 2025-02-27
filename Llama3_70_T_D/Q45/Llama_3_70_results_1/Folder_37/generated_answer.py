def palindromes_between_indices(s):
    s = s[1:5].lower()
    palindromes = set()
    for i in range(5, len(s) * 2 + 1):
        for p in __import__('itertools').product(*[s] * i):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes