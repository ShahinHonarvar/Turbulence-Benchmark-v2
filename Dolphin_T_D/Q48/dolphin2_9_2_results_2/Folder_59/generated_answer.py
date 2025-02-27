def return_binary_or_hexa(t):
    if len(t) < 11:
        return ''
    a, b = (t[0], t[10])
    i = a + 1
    total = 0
    while i < b:
        if i not in t[1:10]:
            total += i
        i += 1
    return bin(total)[2:] if total % 2 != 0 else hex(total)[2:]