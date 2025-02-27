def return_binary_or_hexa(num_tuple):
    a = num_tuple[80]
    b = num_tuple[200]
    missing_sum = sum(set(range(a + 1, b)) - set(num_tuple[80:200]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]