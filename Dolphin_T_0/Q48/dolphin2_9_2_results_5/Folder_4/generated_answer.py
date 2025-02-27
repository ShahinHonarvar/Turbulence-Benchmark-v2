def return_binary_or_hexa(t):
    a, b = (t[49], t[74])
    present = [x for x in t if a + 1 <= x <= b - 1]
    if len(present) == 0:
        return ''
    summ = sum(range(a + 1, b)) - sum(present)
    if summ % 2 == 0:
        return hex(summ)[2:].upper()
    else:
        return bin(summ)[2:]