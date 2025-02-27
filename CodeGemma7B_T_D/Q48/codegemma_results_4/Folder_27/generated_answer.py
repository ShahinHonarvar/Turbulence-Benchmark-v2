import functools

def return_binary_or_hexa(t):
    a = t[86]
    b = t[89]
    sum = functools.reduce(lambda x, y: x + y, [i for i in range(a + 1, b) if i not in t[86:89 + 1]])
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()