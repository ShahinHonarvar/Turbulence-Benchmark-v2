def return_binary_or_hexa(t):
    a = t[49]
    b = t[74]
    total = sum(range(a + 1, b))
    present = sum((i for i in t[50:74] if a < i < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2 == 0:
        return hex(diff)[2:]
    else:
        return bin(diff)[2:]