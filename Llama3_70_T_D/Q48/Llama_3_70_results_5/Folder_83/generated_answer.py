def return_binary_or_hexa(num_tuple):
    a = num_tuple[90]
    b = num_tuple[200]
    num_set = set(num_tuple[90:201])
    total_sum = sum((i for i in range(a + 1, b) if i not in num_set))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]