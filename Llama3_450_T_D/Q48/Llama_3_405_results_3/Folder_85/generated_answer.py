def return_binary_or_hexa(t):
    a = t[1]
    b = t[8]
    total = sum(range(a + 1, b))
    present = sum((i for i in t[2:8] if a < i < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]