def return_binary_or_hexa(t):
    a = t[16]
    b = t[87]
    total_sum = sum((i for i in range(a + 1, b) if i not in t[17:87]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]