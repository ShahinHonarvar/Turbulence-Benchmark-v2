def return_binary_or_hexa(t):
    a = t[0]
    b = t[10]
    total_sum = sum(set(range(a + 1, b)) - set(t[0:11]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()