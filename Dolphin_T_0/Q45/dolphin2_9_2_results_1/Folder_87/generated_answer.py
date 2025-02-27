def palindromes_between_indices(s):
    indices = s[3:10]
    palindromes = set()
    letters = set()
    for i in indices:
        if i.isalpha():
            letters.add(i.lower())
    n = 3
    while n <= len(indices):
        for p in combinations(letters, n):
            p = ''.join(sorted(p))
            while True:
                if ''.join(p[::-1]) == p:
                    palindromes.add(''.join(p))
                if ''.join(p[::-1]) == p:
                    break
                n -= 1
                if n == 2:
                    return palindromes if palindromes else set()
            n += 1
    return palindromes if palindromes else set()