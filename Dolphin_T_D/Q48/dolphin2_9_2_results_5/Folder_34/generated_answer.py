def return_binary_or_hexa(t):
    a, b = (t[60], t[200])
    range_ = [x for x in range(a + 1, b) if x not in t[60:200]]
    if range_ == list(range(a + 1, b)):
        return ''
    s = sum(range_)
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]