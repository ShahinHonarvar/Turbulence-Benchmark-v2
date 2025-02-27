def return_binary_or_hexa(t):
    a = t[44]
    b = t[78]
    total = sum(range(a + 1, b))
    present = sum((i for i in t[44:78] if a < i < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2 != 0:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]