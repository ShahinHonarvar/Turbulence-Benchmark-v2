def return_binary_or_hexa(num_tuple):
    a = num_tuple[36]
    b = num_tuple[85]
    total_sum = sum((i for i in range(a + 1, b) if i not in num_tuple[37:85]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum:
        return hex(total_sum)[2:]
    else:
        return ''