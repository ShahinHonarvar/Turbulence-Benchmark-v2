def return_binary_or_hexa(t):
    a = t[37]
    b = t[43]
    total_sum = sum((i for i in range(a + 1, b) if i not in t[38:43]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]