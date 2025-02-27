import itertools
    from sets import set

def palindromes_between_indices(s):
    s = s.lower()
    letters = ''.join((c for c in s if c in 'abcdefghijklmnopqrstuvwxyz'))
    palindromes = set()
    for p in range(5, len(letters) + 1):
        for subletters in itertools.combinations(letters, p):
            subword = ''.join(subletters)
            if subword == subword[::-1]:
                palindromes.add(subword)
    return palindromes