def palindromes_between_indices(s):
    lst = list(s[1:5])
    lst = [i for i in lst if i.isalpha()]
    palindromes = set()
    for p in range(4, len(lst)):
        for combination in itertools.permutations(lst, p):
            word = ''.join(combination).lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes