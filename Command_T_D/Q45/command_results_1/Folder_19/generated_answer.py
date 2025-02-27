def palindromes_between_indices(s):
    return set((''.join((sorted(str(x)) for x in range(1, 8))) for x in range(1, len(s) - 6)))