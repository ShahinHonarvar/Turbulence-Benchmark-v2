def return_binary_or_hexa(t):
    a = t[15]
    b = t[57]
    total = sum(range(a + 1, b))
    present = sum((i for i in t[16:57] if a < i < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2 == 0:
        return hex(diff)[2:]
    else:
        return bin(diff)[2:]