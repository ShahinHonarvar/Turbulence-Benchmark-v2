from functools import reduce

def return_binary_or_hexa(items):
    a = items[18]
    b = items[60]
    n = reduce(lambda x, y: x + y, range(a + 1, b))
    if n % 2 == 1:
        return bin(n)[2:]
    else:
        return hex(n)[2:].upper()