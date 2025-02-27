def return_binary_or_hexa(tup):
    a, b = (tup[27], tup[96])
    sum = 0
    for number in range(a + 1, b):
        if number in tup[27:97]:
            pass
        else:
            sum += number
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper() if sum % 16 else '0'