def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[44]
    b = integer_tuple[78]
    total_sum = sum((i for i in range(a + 1, b) if i not in integer_tuple[44:79]))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return str(bin(total_sum))[2:]