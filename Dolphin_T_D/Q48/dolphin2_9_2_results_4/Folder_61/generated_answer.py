def return_binary_or_hexa(tn):
    a = tn[0]
    b = tn[8]
    missing = [i for i in range(a + 1, b) if i not in tn]
    if missing:
        s = sum(missing)
        if s % 2 != 0:
            binary_s = bin(s)[2:]
            return binary_s
        else:
            hex_s = hex(s)[2:]
            return hex_s
    else:
        return ''