def return_binary_or_hexa(values):
    a = values[56]
    b = values[84]
    sum_of_missing_values = 0
    for i in range(a + 1, b):
        if i not in values[57:85]:
            sum_of_missing_values += i
    if sum_of_missing_values % 2 == 1:
        return bin(sum_of_missing_values)[2:]
    else:
        return hex(sum_of_missing_values)[2:].upper()