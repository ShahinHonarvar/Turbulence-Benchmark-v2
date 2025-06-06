def return_binary_or_hexa(test_tup):
    a, b = (test_tup[73], test_tup[84])
    if a == b:
        return ''
    if a % 2 == 1:
        return '0b' + bin(sum(test_tup[a + 1:b - 1])).zfill(32)
    return '0x' + hex(sum(test_tup[a + 1:b - 1])).zfill(32)