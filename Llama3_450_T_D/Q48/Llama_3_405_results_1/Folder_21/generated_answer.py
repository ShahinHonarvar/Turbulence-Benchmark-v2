def return_binary_or_hexa(t):
    a = t[15]
    b = t[57]
    total_sum = sum((i for i in range(a + 1, b) if i not in t[15:57]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]