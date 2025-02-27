import itertools
    from string import ascii_letters

def palindromes_between_indices(s):
    s = s[:7]
    s = ''.join((c for c in s if c in ascii_letters))
    palindrome_set = set()
    for p in range(5, len(s) + 1):
        for c in itertools.combinations(s, p):
            if ''.join(c) == ''.join(c[::-1]):
                palindrome_set.add(''.join(c))
    return palindrome_set