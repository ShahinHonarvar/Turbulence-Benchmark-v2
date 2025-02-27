import itertools

def palindromes_between_indices(s):
    substr = ''.join(filter(str.isalpha, s[1:9])).lower()
    palindromes = set()
    for length in range(7, len(substr) + 1):
        for combo in itertools.permutations(substr, length):
            if combo == combo[::-1]:
                palindromes.add(''.join(combo))
    return palindromes