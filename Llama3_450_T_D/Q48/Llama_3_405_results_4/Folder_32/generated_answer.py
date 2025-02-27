def return_binary_or_hexa(t):
    a = t[86]
    b = t[90]
    total_sum = sum((i for i in range(a + 1, b) if i not in t[87:90]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]