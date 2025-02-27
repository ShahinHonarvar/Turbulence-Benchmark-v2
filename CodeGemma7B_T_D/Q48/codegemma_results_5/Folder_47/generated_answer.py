import math

def return_binary_or_hexa(tup):
    a = tup[28]
    b = tup[52]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[29:53]:
            sum += i
    if sum % 2 == 0:
        hex = hex(sum)[2:]
        return hex.upper() if hex[0] == 'F' else hex
    else:
        return bin(sum)[2:]