def return_binary_or_hexa(num_tuple):
    if len(num_tuple) < 81:
        return ''
    a = num_tuple[25]
    b = num_tuple[80]
    total_sum = sum(set(range(a + 1, b)) - set(num_tuple[25:81]))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]