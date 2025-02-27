def return_binary_or_hexa(t):
    a, b = (t[38], t[81])
    missing = [i for i in range(a + 1, b) if i not in t[39:81]]
    if missing:
        total = sum(missing)
        if total % 2 == 1:
            return bin(total)[2:]
        else:
            return hex(total)[2:].upper()
    else:
        return ''