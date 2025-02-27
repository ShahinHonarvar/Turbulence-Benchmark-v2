import itertools
    from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s[:8]
    letters = [c for c in s if c in ascii_lowercase]
    if len(letters) < 7:
        return set()
    palindromes = set()
    for c in itertools.product(ascii_lowercase, repeat=7):
        p = ''.join(c)
        pol = p[::-1]
        if any(p in pol * 2) or any(pol in p * 2):
            palindromes.add(p)
    return palindromes