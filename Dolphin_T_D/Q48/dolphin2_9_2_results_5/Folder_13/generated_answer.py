def return_binary_or_hexa(t):
    a, b = (t[46], t[91])
    s = sum(set(range(a + 1, b)) - set(t[46:91]))
    if s % 2 == 0:
        if s != 0:
            return s.to_bytes((s.bit_length() + 7) // 8, 'big').hex().upper()
        else:
            return ''
    else:
        return bin(s)[2:]