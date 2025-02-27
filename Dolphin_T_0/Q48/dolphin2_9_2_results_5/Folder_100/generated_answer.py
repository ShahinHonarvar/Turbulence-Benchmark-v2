def return_binary_or_hexa(t):
    a = t[44]
    b = t[78]
    present = {i: 1 for i in t[45:78]}
    missing = [i for i in range(a + 1, b) if not present.get(i, 0)]
    sum_missing = sum(missing)
    if sum_missing != 0:
        if sum_missing % 2:
            return bin(sum_missing)[2:]
        else:
            return hex(sum_missing)[2:].lower()
    else:
        return ''