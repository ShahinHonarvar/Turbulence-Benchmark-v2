from collections import defaultdict

def palindromes_between_indices(s):
    eng = 'abcdefghijklmnopqrstuvwxyz'
    chars = defaultdict(int)
    for c in s[:7].lower():
        if c in eng:
            chars[c] += 1
    palindromes = set()
    for len_p in range(4, len(chars) + 1):
        for perm in itertools.permutations(chars.keys(), len_p):
            count = [chars[c] for c in perm]
            if len(set(count)) == 1:
                palindromes.add(''.join(perm))
    return palindromes