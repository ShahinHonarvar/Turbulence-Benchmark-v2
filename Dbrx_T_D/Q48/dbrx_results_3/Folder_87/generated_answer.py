def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[43]
    missing_sum = 0
    present = set(tup[20:44])
    for num in range(a + 1, b):
        if num not in present:
            missing_sum += num
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()