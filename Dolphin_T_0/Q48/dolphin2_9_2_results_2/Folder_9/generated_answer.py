def return_binary_or_hexa(tuple):
    a = tuple[70]
    b = tuple[200]
    sum_integers = sum((i for i in range(a + 1, b - 1) if i not in tuple[70:200]))
    if sum_integers % 2 == 0:
        return bin(sum_integers & -sum_integers)[2:]
    else:
        return hex(sum_integers)[2:]