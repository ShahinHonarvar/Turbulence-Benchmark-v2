def return_binary_or_hexa(t):
    a, b = (t[46], t[91])
    missing_sum = sum(set(range(a + 1, b)) - set(t[46:92]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]