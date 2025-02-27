def return_binary_or_hexa(t):
    a = t[3]
    b = t[8]
    total = sum(range(a + 1, b))
    present = sum((i for i in t[4:8] if a + 1 <= i <= b - 1))
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2 != 0:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]