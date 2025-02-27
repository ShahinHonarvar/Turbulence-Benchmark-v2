def return_binary_or_hexa(t):
    a = t[0]
    b = t[6]
    total_sum = sum((i for i in range(a + 1, b) if i not in t))
    if len(t) != 7 or (a == b - 1 and a > 0) or (a == 0 and len(t) > 1 and isinstance(t[1], int)):
        return ''
    if total_sum % 2:
        return str(bin(total_sum)[2:])
    else:
        return str(hex(total_sum)[2:])