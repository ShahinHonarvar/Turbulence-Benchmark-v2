def return_binary_or_hexa(tupl):
    if len(tupl) < 9:
        return ''
    a = tupl[3]
    b = tupl[8]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in tupl:
            total_sum += i
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]