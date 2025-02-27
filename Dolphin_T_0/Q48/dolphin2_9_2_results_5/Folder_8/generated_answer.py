def return_binary_or_hexa(tupl):
    a = tupl[45]
    b = tupl[48]
    sum_vals = 0
    for i in range(a + 1, b):
        if i not in tupl:
            sum_vals += i
    if sum_vals % 2 == 1:
        return bin(sum_vals)[2:]
    elif sum_vals != 0:
        return hex(sum_vals)[2:].upper()
    else:
        return ''