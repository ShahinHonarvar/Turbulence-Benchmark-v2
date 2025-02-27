def return_binary_or_hexa(tupl):
    a = tupl[86]
    b = tupl[89]
    sum = 0
    for i in range(a + 1, b):
        if i not in tupl[86:89]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]