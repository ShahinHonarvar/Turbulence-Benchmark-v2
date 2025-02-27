def return_binary_or_hexa(tup):
    a, b = (tup[69], tup[97])
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[69:97 + 1]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]