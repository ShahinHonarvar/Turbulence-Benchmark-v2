def return_binary_or_hexa(t):
    a = t[44]
    b = t[67]
    total_sum = sum((i for i in range(a + 1, b) if i not in t[45:67]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]