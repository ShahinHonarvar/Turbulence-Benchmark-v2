def return_binary_or_hexa(tupl):
    a = tupl[20]
    b = tupl[51]
    sum = 0
    for i in range(a + 1, b):
        if i not in tupl:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()