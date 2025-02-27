def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[11], int_tuple[76])
    sum = 0
    for i in range(a + 1, b):
        if i not in int_tuple[11:77]:
            sum += i
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()