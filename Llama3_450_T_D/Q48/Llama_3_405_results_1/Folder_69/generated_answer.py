def return_binary_or_hexa(t):
    a = t[39]
    b = t[43]
    sum_of_missing_numbers = sum((i for i in range(a + 1, b) if i not in t[40:43]))
    if sum_of_missing_numbers == 0:
        return ''
    elif sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:]
    else:
        return bin(sum_of_missing_numbers)[2:]