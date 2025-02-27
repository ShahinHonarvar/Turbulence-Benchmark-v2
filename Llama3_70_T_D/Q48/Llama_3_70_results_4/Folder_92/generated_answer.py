def return_binary_or_hexa(num_tuple):
    a, _, b = num_tuple
    total_sum = sum((i for i in range(a + 1, b) if i not in num_tuple))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]