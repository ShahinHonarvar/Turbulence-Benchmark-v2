def return_binary_or_hexa(t):
    a, b = (t[0], t[10])
    sum_value = sum(set(range(a + 1, b)) - set(t[:11]))
    if sum_value == 0:
        return ''
    elif sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:].rstrip('L')