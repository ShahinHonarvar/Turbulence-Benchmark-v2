def return_binary_or_hexa(t):
    a, b = (t[0], t[2])
    missing_numbers = set(range(a + 1, b)) - set(t[1:2])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''