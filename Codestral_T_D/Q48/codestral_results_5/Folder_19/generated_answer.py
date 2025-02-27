def return_binary_or_hexa(t):
    a, b = (t[1], t[4])
    present = set(t[1:5])
    missing = [x for x in range(a + 1, b) if x not in present]
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()