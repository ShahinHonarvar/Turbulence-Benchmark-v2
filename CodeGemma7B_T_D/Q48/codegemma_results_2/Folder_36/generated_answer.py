def return_binary_or_hexa(tupl):
    a = tupl[110]
    b = tupl[348]
    summ = 0
    for i in range(a + 1, b):
        if i not in tupl[110:348]:
            summ += i
    if summ & 1 == 1:
        return str(summ)[2:]
    else:
        return hex(summ)[2:].upper()