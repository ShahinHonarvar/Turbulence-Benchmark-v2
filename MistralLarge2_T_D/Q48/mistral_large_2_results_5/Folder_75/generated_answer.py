def return_binary_or_hexa(t):
    a, b = (t[20], t[51])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[20:52]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]