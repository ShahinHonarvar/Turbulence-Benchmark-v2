def palindromes_between_indices(s):
    return set((''.join(x) for i in range(3, len(set(s[4:7])) + 1) for x in permutations(s[4:7], i) if x == ''.join(reversed(x))))