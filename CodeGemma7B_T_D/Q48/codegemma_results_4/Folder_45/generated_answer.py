from functools import reduce
from math import log2

def return_binary_or_hexa(tup):
    size = len(tup)
    a, b = (tup[30], tup[200])
    summ = 0
    for i in range(a + 1, b):
        summ += i
    if summ % 2 == 0:
        return hex(summ)[2:]
    else:
        return bin(summ)[2:]