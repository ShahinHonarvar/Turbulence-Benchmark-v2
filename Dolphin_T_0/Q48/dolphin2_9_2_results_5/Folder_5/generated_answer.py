def return_binary_or_hexa(t):
    if len(t) < 9:
        return ''
    a = t[2]
    b = t[8]
    total_sum = sum(range(a + 1, b)) - sum(t[3:8])
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]