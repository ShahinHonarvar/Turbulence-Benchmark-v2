def return_binary_or_hexa(values):
    a = values[57]
    b = values[85]
    sum_num = 0
    for i in range(a + 1, b):
        if i not in values:
            sum_num += i
    if sum_num % 2 == 0:
        return hex(sum_num)[2:]
    else:
        return bin(sum_num)[2:]