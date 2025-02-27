def return_binary_or_hexa(t):
    a = t[46]
    b = t[91]
    total_sum = sum((i for i in range(a + 1, b) if i not in t[47:91]))
    if total_sum == 0:
        return ''
    elif total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]