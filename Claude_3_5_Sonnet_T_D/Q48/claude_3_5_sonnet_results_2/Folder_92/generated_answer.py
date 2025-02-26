def return_binary_or_hexa(t):
    a, b = (t[0], t[2])
    excluded = set(t[1:2])
    total = sum((num for num in range(a + 1, b) if num not in excluded))
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]