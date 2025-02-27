def return_binary_or_hexa(t):
    if t[35] - t[20] + 1 != len(t[20:36]):
        return ''
    return bin(sum(set(range(t[20] + 1, t[35] + 1)) - set(t[20:36])))[2:]