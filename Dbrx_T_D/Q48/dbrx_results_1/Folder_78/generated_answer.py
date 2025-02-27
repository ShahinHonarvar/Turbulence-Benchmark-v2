def return_binary_or_hexa(int_tuple):
    a = int_tuple[62]
    b = int_tuple[96]
    sum = 0
    for i in range(a + 1, b):
        if i not in int_tuple[62:97]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()