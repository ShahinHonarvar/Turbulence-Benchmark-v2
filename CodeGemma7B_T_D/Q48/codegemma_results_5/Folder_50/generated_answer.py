def return_binary_or_hexa(tupl):
    a, b = (tupl[13], tupl[76])
    sum_var = 0
    for i in range(a + 1, b):
        if i not in tupl[13:77]:
            sum_var += i
    if sum_var % 2:
        return bin(sum_var)[2:]
    else:
        return hex(sum_var)[2:].upper()