def return_binary_or_hexa(t):
    a, b = (t[11], t[76])
    missing_sum = sum(set(range(a + 1, b)) - set(t[11:77]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()