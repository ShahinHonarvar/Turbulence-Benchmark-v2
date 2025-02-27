def return_binary_or_hexa(t):
    a = t[36]
    b = t[52]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[37:51]))
    if missing_sum != 0:
        if missing_sum % 2 != 0:
            return bin(missing_sum)[2:]
        else:
            return hex(missing_sum)[2:].upper()
    else:
        return ''