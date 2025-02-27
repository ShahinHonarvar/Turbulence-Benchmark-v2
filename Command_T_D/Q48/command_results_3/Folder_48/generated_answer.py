import re

def return_binary_or_hexa(tup):
    a, b = (tup[933], tup[996])
    s = sum((i for i in range(a + 1, b - 1) if i not in tup[933:996]))
    return (re.sub('0b\\d+', 'b\x01', f'{s:b}'), re.sub('0x\\d+', 'x\x01', f'{s:x}'))