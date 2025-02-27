def return_binary_or_hexa(lst):
    a, b = (lst[69], lst[97])
    present = set(lst[70:97])
    missing = [i for i in range(a + 1, b) if i not in present]
    if not missing:
        return ''
    res = sum(missing)
    if res % 2:
        return bin(res)[2:]
    else:
        return hex(res)[2:].upper()