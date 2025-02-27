def return_binary_or_hexa(tu):
    a = tu[62]
    b = tu[96]
    sum_temp = 0
    for i in range(a + 1, b):
        if i not in tu[62:97]:
            sum_temp += i
    if sum_temp % 2 == 0:
        return hex(sum_temp)[2:].upper()
    else:
        return bin(sum_temp)[2:]