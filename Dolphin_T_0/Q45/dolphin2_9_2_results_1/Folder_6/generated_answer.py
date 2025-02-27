def palindromes_between_indices(s):
    left_slice = s[0:8]
    result = set()
    for i in range(4, len(left_slice) + 1):
        for p in permutations(left_slice, i):
            if ''.join(p).lower() == ''.join(reversed(p)).lower():
                result.add(''.join(p).lower())
    return result