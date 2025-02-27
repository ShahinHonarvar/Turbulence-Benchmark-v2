def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[13]
    b = integer_tuple[70]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in integer_tuple:
            total_sum += i
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]