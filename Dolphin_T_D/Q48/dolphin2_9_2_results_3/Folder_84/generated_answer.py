def return_binary_or_hexa(t):
    a = t[32]
    b = t[44]
    include_indices = [i for i, v in enumerate(t) if a < v < b]
    if set(range(a + 1, b)) == set(include_indices):
        return ''
    s = sum(set(range(a + 1, b + 1)) - set(include_indices))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]