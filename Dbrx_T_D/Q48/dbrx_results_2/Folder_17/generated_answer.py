def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[73]
    b = integer_tuple[84]
    sum = 0
    for i in range(a + 1, b):
        if i not in integer_tuple[73:85]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()