def return_binary_or_hexa(t):
    a = t[1]
    b = t[7]
    total = sum(range(a + 1, b))
    existing = sum((i for i in t[2:7] if a < i < b))
    diff = total - existing
    if diff == 0:
        return ''
    elif diff % 2:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]