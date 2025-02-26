def return_binary_or_hexa(tup):
    a = tup[19]
    b = tup[32]
    missing_nums_sum = sum((num for num in range(a + 1, b) if num not in tup[19:33]))
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    elif missing_nums_sum > 0:
        return hex(missing_nums_sum)[2:]
    else:
        return ''