def return_binary_or_hexa(t):
    a = t[36]
    b = t[54]
    total = sum(range(a + 1, b))
    present = sum((i for i in t[37:54] if a < i < b))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2 == 1:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]