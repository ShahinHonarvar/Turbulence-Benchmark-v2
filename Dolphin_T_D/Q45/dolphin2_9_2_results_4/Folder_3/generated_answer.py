def palindromes_between_indices(s):
    subset = ''.join(filter(str.isalpha, s[7:10]))
    palindromes = set()
    for i in map(''.join, itertools.permutations(subset, 3)):
        if i.lower() == i.lower()[::-1]:
            palindromes.add(i)
    return palindromes