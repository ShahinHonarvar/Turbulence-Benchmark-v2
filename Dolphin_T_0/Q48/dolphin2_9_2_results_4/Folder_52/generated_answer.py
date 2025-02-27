def return_binary_or_hexa(t):
    a = t[38]
    b = t[81]
    total = sum(range(a + 1, b))
    present = sum(t[39:81])
    if total - present == 0:
        return ''
    elif (total - present) % 2 != 0:
        return bin(total - present)[2:]
    else:
        return hex(total - present)[2:]