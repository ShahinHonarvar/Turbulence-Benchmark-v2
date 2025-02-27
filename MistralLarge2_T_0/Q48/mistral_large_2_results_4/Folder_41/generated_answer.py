def return_binary_or_hexa(t):
    a, b = (t[3], t[8])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[3:9]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]