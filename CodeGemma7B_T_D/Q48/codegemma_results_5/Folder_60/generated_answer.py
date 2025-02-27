def return_binary_or_hexa(tuple):
    a = tuple[38]
    b = tuple[52]
    sum = 0
    for j in range(a + 1, b):
        if j not in tuple[38:52]:
            sum += j
    decimal_to_binary = bin(sum)[2:]
    if len(decimal_to_binary) == 0:
        decimal_to_hex = hex(sum)[2:]
        return decimal_to_hex.upper()
    decimal_to_hex = hex(sum)[2:]
    return decimal_to_binary