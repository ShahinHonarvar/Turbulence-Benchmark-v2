def palindromes_between_indices(s):
    palindromes = set()
    sub = s[5:8]
    n = len(sub)
    permutations = [''.join(p) for p in permutations(sub)]
    for p in permutations:
        for i in range(n - 1, 3, -1):
            for j in range(n - i + 1):
                sub = p[j:j + i]
                sub = sub.lower()
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes