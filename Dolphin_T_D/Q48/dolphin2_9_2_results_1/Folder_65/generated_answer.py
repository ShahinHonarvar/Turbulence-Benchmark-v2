def return_binary_or_hexa(t):
    a, b = (t[51], t[76])
    missing = [num for num in range(a + 1, b) if num not in t[52:76]]
    if not missing:
        return ''
    s = sum(missing)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]