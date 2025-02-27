def return_binary_or_hexa(t):
    a, b = (t[22], t[24])
    missing_sum = sum((i for i in range(a + 1, b) if i not in set(t[22:25])))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()