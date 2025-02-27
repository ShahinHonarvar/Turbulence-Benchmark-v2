def return_binary_or_hexa(tupl):
    a = tupl[37]
    b = tupl[43]
    sum = 0
    for i in range(a + 1, b):
        if i not in tupl:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]