def palindromes_between_indices(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    substring = s[2:6]
    palindromes = set()
    for p in permutations(substring):
        if ''.join(p) == ''.join(p)[::-1] and len(''.join(p)) >= 3:
            palindromes.add(''.join(p).lower())
    return palindromes