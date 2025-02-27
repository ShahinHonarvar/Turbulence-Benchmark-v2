def return_binary_or_hexa(tu):
    n = tu[4] - tu[1] - 1
    s = 0
    for i in range(tu[1] + 1, tu[4]):
        if i not in tu:
            s += i
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]