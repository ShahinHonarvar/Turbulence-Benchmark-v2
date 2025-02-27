def return_binary_or_hexa(tuple):
    a = tuple[13]
    b = tuple[35]
    if all((x in tuple for x in range(a + 1, b))):
        return ''
    else:
        number = sum((x for x in range(a + 1, b + 1) if x not in tuple[13:36]))
        if number % 2 == 0:
            return hex(number)[2:]
        else:
            return bin(number)[2:]