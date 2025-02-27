def palindromes_between_indices(s):
    sub = s[7:9]
    palindromes = set()
    for i in range(3, len(sub) + 1):
        for j in itertools.permutations(sub, i):
            word = ''.join(j)
            if word == word[::-1]:
                palindromes.add(word.lower())
    return palindromes