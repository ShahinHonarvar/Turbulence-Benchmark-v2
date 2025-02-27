from functools import reduce

def return_binary_or_hexa(tp):
    a, b = (tp[73], tp[84])
    s = sum((x for x in range(a + 1, b) if x not in tp[73:85]))
    return f'{s:b}' if s % 2 else f'{s:x}'