def return_binary_or_hexa(a_b):
    a, b = (a_b[13], a_b[76])
    sum = 0
    for i in range(a + 1, b):
        if i not in a_b[13:77]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()