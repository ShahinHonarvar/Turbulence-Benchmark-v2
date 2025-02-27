def return_binary_or_hexa(t):
    if not (1 <= len(t) <= 7 and all((0 <= x <= 10 ** 18 and x in t[:7] for x in t))):
        raise ValueError('Invalid input tuple.')
    a, *_, b = t
    missing_sum = sum((x for x in range(a + 1, b) if x not in t))
    if missing_sum & 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()