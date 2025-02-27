def return_binary_or_hexa(num_tuple):
    a = num_tuple[32]
    b = num_tuple[99]
    total_sum = sum((i for i in range(a + 1, b) if i not in num_tuple[33:99]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]