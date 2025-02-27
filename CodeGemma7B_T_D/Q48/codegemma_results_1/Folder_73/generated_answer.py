from functools import reduce

def return_binary_or_hexa(arg):
    s = set(range(arg[10] + 1, arg[76])) - set(arg[10:76])
    count = len(s)
    return bin(reduce(lambda x, y: x + y, s))[2:] if count % 2 == 1 else hex(reduce(lambda x, y: x + y, s))[2:].upper() if len(hex(reduce(lambda x, y: x + y, s))[2:]) % 2 == 1 else hex(reduce(lambda x, y: x + y, s))[2:]