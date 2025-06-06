def return_binary_or_hexa(test_tup):
    a, b = (test_tup[46], test_tup[91])
    if a == b:
        return ''
    if a % 2 == 1:
        return '0b' + bin(a + 1 + (b - a - 1) % 2).zfill(8)
    return '0x' + hex(a + 1 + (b - a - 1) % 2)