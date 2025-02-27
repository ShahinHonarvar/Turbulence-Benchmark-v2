def return_binary_or_hexa(t):
    a, b = (t[90], t[200])
    total = sum((i for i in range(a + 1, b) if i not in t[91:201]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]