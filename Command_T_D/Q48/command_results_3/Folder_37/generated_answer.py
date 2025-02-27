import re

def return_binary_or_hexa(tup):
    s = sum((x for x in range(tup[2] + 1, tup[7] - 1)))
    if s % 2:
        return re.sub('([01]0+)', '\x01', bin(s)[2:])
    else:
        return re.sub('([0-9A-F]+)', '\x01', hex(s))