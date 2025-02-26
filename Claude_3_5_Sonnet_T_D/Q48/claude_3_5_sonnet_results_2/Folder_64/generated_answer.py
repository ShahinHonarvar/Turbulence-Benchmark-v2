def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[5])
    excluded_sum = sum(set(range(a + 1, b)) - set(tup[:6]))
    if excluded_sum == 0:
        return ''
    elif excluded_sum % 2 == 1:
        return bin(excluded_sum)[2:]
    else:
        return hex(excluded_sum)[2:].rstrip('L')