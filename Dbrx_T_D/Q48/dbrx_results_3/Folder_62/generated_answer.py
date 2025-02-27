def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[50]
    b = integer_tuple[92]
    sum = 0
    for i in range(a + 1, b):
        if i not in integer_tuple[50:93]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()