def return_binary_or_hexa(t):
    a = t[35]
    b = t[64]
    sum_of_missing_numbers = sum((i for i in range(a + 1, b) if i not in t[36:64]))
    if sum_of_missing_numbers == 0:
        return ''
    elif sum_of_missing_numbers % 2 != 0:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]