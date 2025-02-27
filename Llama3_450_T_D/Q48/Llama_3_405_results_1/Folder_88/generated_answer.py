def return_binary_or_hexa(t):
    a = t[3]
    b = t[9]
    s = set(t[3:10])
    total_sum = sum((i for i in range(a + 1, b) if i not in s))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]