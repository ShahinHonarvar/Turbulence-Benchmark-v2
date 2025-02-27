def return_binary_or_hexa(t):
    if 36 < 54 < len(t) and t[36] + 1 < t[54] - 1:
        s = sum(set(range(t[36] + 1, t[54])) - set(t[37:54]))
        if s % 2:
            return bin(s)[2:]
        else:
            return hex(s)[2:]
    return ''