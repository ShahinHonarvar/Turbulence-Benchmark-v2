def palindromes_between_indices(s):
    s = s[2:4].lower()
    palindromes = set()
    for i in range(3, 1000):
        for p in itertools.product(string.ascii_lowercase, repeat=i):
            if ''.join(p) == ''.join(p)[::-1] and set(''.join(p)).issubset(set(s)):
                palindromes.add(''.join(p))
    return palindromes