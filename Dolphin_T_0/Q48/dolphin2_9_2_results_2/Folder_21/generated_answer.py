def return_binary_or_hexa(input_tuple):
    a = input_tuple[15]
    b = input_tuple[57]
    total_sum = sum((i for i in range(a + 1, b) if i not in input_tuple[15:58]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]