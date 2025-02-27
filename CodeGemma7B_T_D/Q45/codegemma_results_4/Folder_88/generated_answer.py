def palindromes_between_indices(text):
    ps = set()
    for i in range(3, 8):
        for j in range(i + 1, 8):
            text_slice = text[i:j + 1]
            if all((c.lower() in 'abcdefghijklmnopqrstuvwxyz' for c in text_slice)):
                palindromes = set()
                for perm in itertools.permutations(text_slice):
                    palindromes.add(''.join(perm))
                ps |= palindromes
    return ps