def return_binary_or_hexa(cle_t):
    a = cle_t[110]
    b = cle_t[348]
    sum = 0
    for i in range(a + 1, b):
        if i not in cle_t:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]