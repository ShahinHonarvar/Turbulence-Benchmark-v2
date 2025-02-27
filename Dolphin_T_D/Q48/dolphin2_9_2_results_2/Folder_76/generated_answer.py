def return_binary_or_hexa(tuple):
    a = tuple[450]
    b = tuple[905]
    result = sum(set(range(a + 1, b)) - set(tuple[450:906]))
    if result % 2 == 0:
        return hex(result)[2:]
    else:
        return bin(result)[2:]