def return_binary_or_hexa(tupl):
    a = tupl[34]
    b = tupl[69]
    sum = 0
    for i in range(a + 1, b):
        if i not in tupl[34:70]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]