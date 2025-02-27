def dict_to_list(d):
    l = []
    for k in d.keys():
        l.extend([k] * d[k])
    return l

def return_binary_or_hexa(lst):
    if len(lst) < 53:
        return ''
    a, b = (lst[36], lst[52])
    if all((x in lst[36:53] for x in range(a + 1, b))):
        return ''
    s = 0
    for i in range(a + 1, b):
        if i not in lst[36:53]:
            s += i
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()