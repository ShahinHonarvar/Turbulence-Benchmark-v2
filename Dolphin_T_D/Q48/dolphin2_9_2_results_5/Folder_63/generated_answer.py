def return_binary_or_hexa(num_tuple):
    a = num_tuple[81]
    b = num_tuple[86]
    missing_sum = sum(set(range(a + 1, b)) - set(num_tuple[82:86]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()