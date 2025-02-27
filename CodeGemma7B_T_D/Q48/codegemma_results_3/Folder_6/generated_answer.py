def return_binary_or_hexa(tu):
    a, b = (tu[20], tu[93])
    res = 0
    for i in range(a + 1, b):
        if i not in tu[20:94]:
            res += i
    if res & 1:
        return bin(res)[2:]
    return hex(res)[2:].upper() if res <= 15 else hex(res)[2:]