import itertools

def palindromes_between_indices(s):
    s = s[4:10].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(5, len(s) + 1):
        for combination in itertools.permutations(s, length):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    return palindromes