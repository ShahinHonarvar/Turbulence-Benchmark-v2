def return_binary_or_hexa(tupl):
    a = tupl[44]
    b = tupl[67]
    summ = 0
    for num in range(a + 1, b):
        if num not in tupl:
            summ += num
    if summ % 2 == 1:
        return bin(summ)[2:]
    else:
        return hex(summ)[2:].upper()