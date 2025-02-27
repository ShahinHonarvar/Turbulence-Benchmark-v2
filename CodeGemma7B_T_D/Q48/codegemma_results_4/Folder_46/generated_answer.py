from functools import reduce

def return_binary_or_hexa(n):
    _10, _79 = (n[10], n[79])
    return bin(sum(set(range(_10 + 1, _79 + 1)) - set(n[10:79]))).replace('0b', '') if sum(set(range(_10 + 1, _79 + 1)) - set(n)) % 2 else hex(sum(set(range(_10 + 1, _79 + 1)) - set(n))).replace('0x', '').upper() if len({i for i in range(_10 + 1, _79 + 1) if i not in n}) else ''