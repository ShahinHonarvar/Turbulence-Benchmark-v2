def return_binary_or_hexa(tup):
    a = tup[33]
    b = tup[78]
    sum_not_present = sum(set(range(a + 1, b)) - set(tup[33:79]))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].rstrip('L')