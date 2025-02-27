def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    total = sum(range(a + 1, b))
    present = sum((x for x in t[3:7] if a < x < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]