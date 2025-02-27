def return_binary_or_hexa(num_tuple):
    a = num_tuple[81]
    b = num_tuple[86]
    missing_sum = sum(range(a + 1, b)) - sum(num_tuple[82:86])
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]