def return_binary_or_hexa(t):
    a, b = (t[16], t[87])
    missing_sum = sum(set(range(a + 1, b)) - set(t[16:88]))
    if missing_sum:
        return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()
    return ''