def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[16], int_tuple[87])
    if a > b:
        return ''
    present = sum((1 for i in range(a + 1, b) if i in int_tuple[16:87 + 1]))
    if present == b - a - 1:
        return ''
    total_sum = sum(range(a + 1, b))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]