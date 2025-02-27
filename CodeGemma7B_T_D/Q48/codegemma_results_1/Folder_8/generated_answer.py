def return_binary_or_hexa(tupl):
    a, b = (tupl[45], tupl[48])
    sum = 0
    for x in range(a + 1, b):
        if x not in tupl[45:49]:
            sum += x
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()