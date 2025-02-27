def return_binary_or_hexa(tup):
    a = tup[39]
    b = tup[43]
    numbers = set(tup[40:43])
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum > 0:
        return hex(missing_sum)[2:]
    return ''