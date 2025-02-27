def return_binary_or_hexa(tup):
    a = tup[56]
    b = tup[88]
    present_set = set(tup[57:88])
    total = 0
    for num in range(a + 1, b):
        if num not in present_set:
            total += num
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()