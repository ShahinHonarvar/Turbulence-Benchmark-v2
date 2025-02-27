def return_binary_or_hexa(t):
    a, b = (t[7], t[9])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[7:10]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum > 0:
        return hex(missing_sum)[2:]
    else:
        return ''