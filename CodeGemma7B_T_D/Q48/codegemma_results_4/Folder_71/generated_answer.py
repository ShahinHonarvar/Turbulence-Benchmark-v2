from functools import reduce

def return_binary_or_hexa(tuple1):
    a, b = (tuple1[20], tuple1[35])
    sum = reduce(lambda x, y: x + y, range(a + 1, b))
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]