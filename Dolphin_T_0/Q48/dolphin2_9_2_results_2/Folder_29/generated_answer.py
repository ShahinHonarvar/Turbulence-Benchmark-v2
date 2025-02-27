def return_binary_or_hexa(lst):
    if len(lst) < 99:
        return ''
    a = lst[70]
    b = lst[98]
    if b - a != len(lst[71:98]):
        return ''
    d = [i for i in range(a + 1, b) if i not in lst[71:99]]
    s = sum(d)
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]