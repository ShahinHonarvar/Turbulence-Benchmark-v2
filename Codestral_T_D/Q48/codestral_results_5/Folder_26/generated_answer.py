def return_binary_or_hexa(tup):
    a, b = (tup[68], tup[99])
    s = set(tup[68 + 1:99])
    missing_sum = sum((x for x in range(a + 1, b) if x not in s))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]