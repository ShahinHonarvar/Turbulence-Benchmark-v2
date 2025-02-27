from typing import Tuple

def return_binary_or_hexa(tuples):
    a, b = (tuples[70], tuples[98])
    sum = 0
    for i in range(a + 1, b):
        if i not in tuples[70:99]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    return hex(sum)[2:].upper()