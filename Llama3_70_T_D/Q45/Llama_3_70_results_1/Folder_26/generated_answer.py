def palindromes_between_indices(s):
    s = s[4:7].lower()
    palindromes_set = set()
    for i in range(3, len(s) + 1):
        for subset in itertools.permutations(s, i):
            word = ''.join(subset)
            if word == word[::-1]:
                palindromes_set.add(word)
    return palindromes_set