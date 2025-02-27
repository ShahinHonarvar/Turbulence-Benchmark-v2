def return_binary_or_hexa(num_tuple):
    a, b = (num_tuple[32], num_tuple[99])
    total_sum = sum(set(range(a + 1, b)) - set(num_tuple[32:100]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]