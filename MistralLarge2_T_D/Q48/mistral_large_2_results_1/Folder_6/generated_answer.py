def return_binary_or_hexa(t):
    a = t[20]
    b = t[93]
    sum_values = sum(set(range(a + 1, b)) - set(t[20:94]))
    if sum_values == 0:
        return ''
    elif sum_values % 2 == 1:
        return bin(sum_values)[2:]
    else:
        return hex(sum_values)[2:].upper()