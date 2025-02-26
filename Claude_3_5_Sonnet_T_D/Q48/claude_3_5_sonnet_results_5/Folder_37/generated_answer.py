def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    sum_not_present = sum((num for num in range(a + 1, b) if num not in t[2:8]))
    if sum_not_present == 0:
        return ''
    if sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]