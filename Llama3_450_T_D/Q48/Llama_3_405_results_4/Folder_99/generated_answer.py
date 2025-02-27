def return_binary_or_hexa(tup):
    a = tup[427]
    b = tup[669]
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[427:669]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]