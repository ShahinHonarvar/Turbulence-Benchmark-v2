def return_binary_or_hexa(tu):
    a, b = (tu[18], tu[52])
    missing = [n for n in range(a + 1, b) if n not in tu[19:52]]
    s = sum(missing)
    if not missing:
        return ''
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]