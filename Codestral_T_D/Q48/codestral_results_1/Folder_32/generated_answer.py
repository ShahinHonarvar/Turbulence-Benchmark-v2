def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[90]
    missing_numbers = set(range(a + 1, b)) - set(tup[86:90])
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]