def return_binary_or_hexa(t):
    if t[40] + 1 <= t[200]:
        return ''
    s = sum(set(range(t[40] + 1, t[200] + 1)) - set(t[40:201]))
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper()