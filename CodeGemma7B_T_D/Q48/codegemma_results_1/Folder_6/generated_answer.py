def return_binary_or_hexa(tup):
    if not tup or tup[20] >= tup[93]:
        return ''
    a, b = (tup[20] + 1, tup[93] - 1)
    XOR_sum = 0
    for index in range(len(tup)):
        if index >= 20 and index <= 93:
            XOR_sum ^= tup[index]
    missing_sum = b - a + 1 - XOR_sum
    if missing_sum >= 0 and missing_sum <= 9:
        return str(missing_sum)
    elif missing_sum >= 10 and missing_sum <= 255:
        return hex(missing_sum)[2:]
    else:
        missing_sum_binary = bin(missing_sum)[2:]
        while missing_sum_binary[0] == '0':
            missing_sum_binary = missing_sum_binary[1:]
        return missing_sum_binary