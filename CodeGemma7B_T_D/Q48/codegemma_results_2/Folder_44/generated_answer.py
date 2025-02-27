def return_binary_or_hexa(tup):
    a, b = (tup[36], tup[52])
    xor_sum = 0
    for i in range(a + 1, b):
        if i not in tup[36:53]:
            xor_sum ^= i
    return '0b' + bin(xor_sum)[2:].zfill(b - (a + 1)) if xor_sum % 2 != 0 else '0x' + hex(xor_sum)[2:].zfill((b - (a + 1)) // 4) if xor_sum % 2 == 0 else ''