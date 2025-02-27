def return_binary_or_hexa(t):
    a = t[1]
    b = t[4]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[1:5]))
    if missing_sum:
        return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()
    return ''