def return_binary_or_hexa(t):
    a, b = (t[0], t[10])
    total_sum = sum((i for i in range(a + 1, b) if i not in t[:11]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]