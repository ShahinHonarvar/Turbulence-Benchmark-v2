def return_binary_or_hexa(t):
    a, b = (t[0], t[6])
    total = sum(range(a + 1, b)) - sum(t[1:6])
    if total == 0 or (total % 2 == 0 and all((i + 1 in t for i in range(a, b - 1)))):
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]