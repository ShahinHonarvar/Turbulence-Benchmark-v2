from itertools import product

def palindrome_of_length_at_least_n(str):
    all_possibilities = product('abcdefghijklmnopqrstuvwxyz', repeat=2)
    palindrome_format = ''.join(map(''.join, all_possibilities))
    expected_format = '%s%s' % (palindrome_format, palindrome_format[::-1])
    for p in [w for w in expected_format if w in str]:
        if len(p) >= 78:
            return {p.lower().upper()}
    return set()