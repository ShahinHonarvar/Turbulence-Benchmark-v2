def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[76]
    missing_sum = sum((num for num in range(a + 1, b) if num not in tup[14:76]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]