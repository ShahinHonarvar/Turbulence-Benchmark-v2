def return_binary_or_hexa(t):
    a, b = (t[33], t[78])
    if a >= b:
        return ''
    present = set(t[33:79])
    missing = set(range(a + 1, b))
    missing -= present
    if not missing:
        return ''
    sum_of_missing = sum(missing)
    if sum_of_missing % 2:
        return bin(sum_of_missing).split('0b')[1]
    else:
        return hex(sum_of_missing).split('0x')[1]